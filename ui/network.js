new Vue({
  el: "#app",
  data: {
    nodes: [],
    newNodeUrl: "",
    error: null,
    success: null,
  },
  methods: {
    onAddNode: function () {
      // Add node as peer node to local node server
      var vm = this;
      axios
        .post("/node", { node: this.newNodeUrl })
        .then(function (response) {
          vm.success = "Stored node successfully.";
          vm.error = null;
          vm.nodes = response.data.all_nodes;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
        });
    },
    onLoadNodes: function () {
      // Load all peer nodes of the local node server
      var vm = this;
      axios
        .get("/nodes")
        .then(function (response) {
          vm.success = "Fetched nodes successfully.";
          vm.error = null;
          vm.nodes = response.data.all_nodes;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
        });
    },
    onRemoveNode: function (node_url) {
      // Remove node as a peer node
      var vm = this;
      axios
        .delete("/node/" + node_url)
        .then(function (response) {
          vm.success = "Deleted node successfully.";
          vm.error = null;
          vm.nodes = response.data.all_nodes;
        })
        .catch(function (error) {
          vm.success = null;
          vm.error = error.response.data.message;
        });
    },
  },
});
