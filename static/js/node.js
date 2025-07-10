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
    onCreateWallet() {
      const vm = this;
      vm.walletLoading = true;
      axios
        .post("/wallet")
        .then((res) => {
          vm.error = null;
          vm.success = `Created Wallet! Public Key: ${res.data.public_key}, Private Key: ${res.data.private_key}`;
          vm.wallet = {
            public_key: res.data.public_key,
            private_key: res.data.private_key,
          };
          vm.funds = res.data.funds;
          vm.walletLoading = false;
        })
        .catch((err) => {
          vm.success = null;
          vm.error = err.response?.data?.message || "Error creating wallet.";
          vm.wallet = null;
          vm.walletLoading = false;
        });
    },
    onLoadWallet() {
      const vm = this;
      vm.walletLoading = true;
      axios
        .get("/wallet")
        .then((res) => {
          vm.error = null;
          vm.success = `Loaded Wallet! Public Key: ${res.data.public_key}, Private Key: ${res.data.private_key}`;
          vm.wallet = {
            public_key: res.data.public_key,
            private_key: res.data.private_key,
          };
          vm.funds = res.data.funds;
          vm.walletLoading = false;
        })
        .catch((err) => {
          vm.success = null;
          vm.error = err.response?.data?.message || "Error loading wallet.";
          vm.wallet = null;
          vm.walletLoading = false;
        });
    },
    onSendTx() {
      const vm = this;
      vm.txLoading = true;
      axios
        .post("/transaction", {
          recipient: vm.outgoingTx.recipient,
          amount: vm.outgoingTx.amount,
        })
        .then((res) => {
          vm.success = res.data.message;
          vm.error = null;
          vm.funds = res.data.funds;
          vm.txLoading = false;
        })
        .catch((err) => {
          vm.success = null;
          vm.error = err.response?.data?.message || "Transaction failed.";
          vm.txLoading = false;
        });
    },
    onMine() {
      const vm = this;
      axios
        .post("/mine")
        .then((res) => {
          vm.success = res.data.message;
          vm.error = null;
          vm.funds = res.data.funds;
        })
        .catch((err) => {
          vm.success = null;
          vm.error = err.response?.data?.message || "Mining failed.";
        });
    },
    onResolve() {
      const vm = this;
      axios
        .post("/resolve-conflicts")
        .then((res) => {
          vm.success = res.data.message;
          vm.error = null;
        })
        .catch((err) => {
          vm.success = null;
          vm.error = err.response?.data?.message || "Conflict resolution failed.";
        });
    },
    onLoadData() {
      const vm = this;
      vm.dataLoading = true;
      const url = this.view === "chain" ? "/chain" : "/transactions";
      axios
        .get(url)
        .then((res) => {
          if (vm.view === "chain") {
            vm.blockchain = res.data;
          } else {
            vm.openTransactions = res.data;
          }
          vm.dataLoading = false;
        })
        .catch(() => {
          vm.error = "Something went wrong.";
          vm.dataLoading = false;
        });
    },
  },
});
