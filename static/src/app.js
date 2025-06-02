import Vue from "vue";
import WalletActions from "./components/WalletActions.js";
import TransactionForm from "./components/TransactionForm.js";
import BlockchainView from "./components/BlockchainView.js";
import TransactionsView from "./components/TransactionsView.js";

new Vue({
  el: "#app",
  components: {
    WalletActions,
    TransactionForm,
    BlockchainView,
    TransactionsView,
  },
  template: `
    <div class="container mx-auto px-4 py-8">
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Manage your Blockchain</h1>
      </div>
      
      <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">{{ error }}</div>
      <div v-if="success" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">{{ success }}</div>
      
      <wallet-actions 
        :walletLoading="walletLoading" 
        :funds="funds"
        @create-wallet="onCreateWallet"
        @load-wallet="onLoadWallet"
      ></wallet-actions>
      
      <transaction-form
        v-if="wallet"
        :txLoading="txLoading"
        :outgoingTx="outgoingTx"
        @send-tx="onSendTx"
      ></transaction-form>
      
      <div class="mb-6">
        <ul class="flex border-b">
          <li class="-mb-px mr-1">
            <a class="inline-block py-2 px-4 font-semibold" 
              :class="{'border-b-2 border-blue-500 text-blue-600': view === 'chain', 'text-blue-500 hover:text-blue-800': view !== 'chain'}" 
              href="#" @click="view = 'chain'">Blockchain</a>
          </li>
          <li class="mr-1">
            <a class="inline-block py-2 px-4 font-semibold" 
              :class="{'border-b-2 border-blue-500 text-blue-600': view === 'tx', 'text-blue-500 hover:text-blue-800': view !== 'tx'}" 
              href="#" @click="view = 'tx'">Open Transactions</a>
          </li>
        </ul>
      </div>
      
      <div class="mb-6">
        <div class="space-x-2">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" 
            @click="onLoadData">{{ view === 'chain' ? 'Load Blockchain' : 'Load Transactions' }}</button>
          <button v-if="view === 'chain' && wallet" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" 
            @click="onMine">Mine Coins</button>
        </div>
      </div>
      
      <blockchain-view 
        v-if="view === 'chain' && !dataLoading" 
        :blockchain="blockchain"
        :showElement="showElement"
      ></blockchain-view>
      
      <transactions-view 
        v-if="view === 'tx' && !dataLoading" 
        :transactions="openTransactions"
        :showElement="showElement"
      ></transactions-view>
      
      <div v-if="dataLoading" class="lds-ring">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </div>
  `,
  data: {
    blockchain: [],
    openTransactions: [],
    wallet: null,
    view: "chain",
    walletLoading: false,
    txLoading: false,
    dataLoading: false,
    showElement: null,
    error: null,
    success: null,
    funds: 0,
    outgoingTx: {
      recipient: "",
      amount: 0,
    },
  },
  computed: {
    loadedData: function () {
      return this.view === "chain" ? this.blockchain : this.openTransactions;
    },
  },
  methods: {
    onCreateWallet: function () {
      const vm = this;
      this.walletLoading = true;
      axios
        .post("/wallet")
        .then(function (response) {
          vm.error = null;
          vm.success = "Created Wallet! Public Key: " + response.data.public_key + ", Private Key: " + response.data.private_key;
          vm.wallet = {
            public_key: response.data.public_key,
            private_key: response.data.private_key,
          };
          vm.funds = response.data.funds;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
          vm.wallet = null;
        })
        .finally(() => {
          vm.walletLoading = false;
        });
    },

    onLoadWallet: function () {
      const vm = this;
      this.walletLoading = true;
      axios
        .get("/wallet")
        .then(function (response) {
          vm.error = null;
          vm.success = "Loaded Wallet! Public Key: " + response.data.public_key + ", Private Key: " + response.data.private_key;
          vm.wallet = {
            public_key: response.data.public_key,
            private_key: response.data.private_key,
          };
          vm.funds = response.data.funds;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
          vm.wallet = null;
        })
        .finally(() => {
          vm.walletLoading = false;
        });
    },

    onSendTx: function () {
      const vm = this;
      this.txLoading = true;
      axios
        .post("/transaction", {
          recipient: this.outgoingTx.recipient,
          amount: this.outgoingTx.amount,
        })
        .then(function (response) {
          vm.error = null;
          vm.success = response.data.message;
          console.log(response.data);
          vm.funds = response.data.funds;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
        })
        .finally(() => {
          vm.txLoading = false;
        });
    },

    onMine: function () {
      const vm = this;
      axios
        .post("/mine")
        .then(function (response) {
          vm.error = null;
          vm.success = response.data.message;
          console.log(response.data);
          vm.funds = response.data.funds;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
        });
    },

    onLoadData: function () {
      const vm = this;
      this.dataLoading = true;
      const url = this.view === "chain" ? "/chain" : "/transaction";

      axios
        .get(url)
        .then(function (response) {
          if (vm.view === "chain") {
            vm.blockchain = response.data;
          } else {
            vm.openTransactions = response.data;
          }
        })
        .catch(function () {
          vm.error = "Something went wrong.";
        })
        .finally(() => {
          vm.dataLoading = false;
        });
    },
  },
});
