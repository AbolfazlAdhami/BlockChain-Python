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
