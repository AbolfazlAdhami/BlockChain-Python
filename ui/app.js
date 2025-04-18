new Vue({
  el: "#app",
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
      const url = this.view === "chain" ? "/chain" : "/transactions";

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
