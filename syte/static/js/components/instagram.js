var InstagramPanel = function($linkEl) {
  this.initialize($linkEl);

  this.fetchData = function() {
    var _this = this;

    require(["json!/instagram/",
            "text!templates/instagram-view.html",
            "text!templates/instagram-view-more.html"],
      function(instagram_data, instagram_view, instagram_view_more) {
        if (instagram_data.media == 0){
          window.location = href;
          return;
        }

        var template = Handlebars.compile(instagram_view),
            moreTemplate,
            user_counts = instagram_data.user['counts'];

        user_counts.media = numberWithCommas(user_counts.media);
        user_counts.followed_by = numberWithCommas(user_counts.followed_by);
        user_counts.follows = numberWithCommas(user_counts.follows);

        $.each(instagram_data.media, function(i, p) {
           p.formated_date = moment.unix(parseInt(p.created_time)).fromNow();
        });

        _this.$modal = $(template(instagram_data)).modal();
        _this.setupModal(_this.$modal);
        _this.showing = true;

        moreTemplate = Handlebars.compile(instagram_view_more);

        $('#load-more-pics').click(function(e) {
          next = $(this).attr('data-control-next');

          var spinner = new Spinner(spin_opts).spin();
          $('#load-more-pics').append(spinner.el);

          $.getJSON('/instagram/' + next, function(data) {

            $.each(data.media, function(i, p) {
               p.formated_date = moment.unix(parseInt(p.created_time)).fromNow();
            });

            $('.instagram .profile-shots').append(more_template(data));

            if (data.pagination && data.pagination['next_max_id'])
               $('#load-more-pics').attr('data-control-next', data.pagination['next_max_id']);
            else
               $('#load-more-pics').remove();

            _this.linkSpinner.stop();
          });
        });

        _this.linkSpinner.stop();
      });
  };

  this.fetchData();
};

InstagramPanel.prototype = basePanel;
