var GithubPanel = function(linkEl) {
  this.initialize(linkEl);

  this.fetchData = function() {
    var _this = this;
    require(["json!/github/gkoo", "text!templates/github-profile.html"],
      function(github_data, github_view) {
        var template;
        if (github_data.error || github_data.length === 0) {
          window.location = href;
          return;
        }

        template = Handlebars.compile(github_view);
        github_data.user.following = numberWithCommas(github_data.user.following);
        github_data.user.followers = numberWithCommas(github_data.user.followers);

        _this.$modal = $(template(github_data)).modal();
        _this.setupModal(_this.$modal);
        /*
        _this.$modal.on('hidden', function () {
          $(this).remove();
          if (currSelection === 'github') {
            adjustSelection('home');
          }
        });
        */
        _this.showing = true;

        _this.linkSpinner.stop();

      });
  };

  this.fetchData();
};

GithubPanel.prototype = basePanel;
