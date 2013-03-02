var $url,

allComponents = [
  'instagram',
  'twitter',
  'github',
  //'dribbble',
  //'lastfm',
  //'soundcloud',
  //'bitbucket',
  //'foursquare',
  //'tent'
  'about'
],

panels = {},

currSelection = 'home',

setupLinks = function() {
  $('header').click(function(e) {
    var $target = $(e.target),
        panel,
        newSelection,
        url;

    e.preventDefault();
    newSelection = $target.attr('data-site'); // e.g. "instagram", "twitter", etc.

    if (e.which === 2 || !$target.hasClass('nav-link') || currSelection === newSelection) {
      return;
    }

    currSelection = newSelection;

    panel = panels[currSelection]; // holds the Panel object for this site.

    adjustSelection(currSelection);
    if (panel) {
      panel.show();
    }
    else {
      if($target.attr('id') === 'twitter-link' && twitter_integration_enabled) {
        panels.twitter = new TwitterPanel($target);
      }
      else if($target.attr('id') === 'github-link' && github_integration_enabled) {
        panels.github = new GithubPanel($target);
      }
      else if($target.attr('id') === 'instagram-link' && instagram_integration_enabled) {
        panels.instagram = new InstagramPanel($target);
      }
    }

    /*
    return;
    if (this.id === 'home-link' && window.location.pathname === '/') {
      adjustSelection('home');
    }
    else if(this.id === 'instagram-link' && instagram_integration_enabled) {
      adjustSelection('instagram');
      //panels.instagram = setupInstagram(this);
    }
    else if (twitter_integration_enabled && (url.attr('host') === 'twitter.com' || url.attr('host') === 'www.twitter.com')) {
      adjustSelection('twitter');
      setupTwitter(url, this);
    }
    else if (github_integration_enabled && (url.attr('host') === 'github.com' || url.attr('host') === 'www.github.com')) {
      adjustSelection('github');
      setupGithub(url, this);
    }
    else if (dribbble_integration_enabled && (url.attr('host') === 'dribbble.com' || url.attr('host') === 'www.dribbble.com')) {
      adjustSelection('dribbble');
      setupDribbble(url, this);
    }
    else if (lastfm_integration_enabled && (url.attr('host') === 'lastfm.com' || url.attr('host') === 'www.lastfm.com')) {
      adjustSelection('lastfm');
      setupLastfm(url, this);
    }
    else if (soundcloud_integration_enabled && (url.attr('host') === 'soundcloud.com' || url.attr('host') === 'www.soundcloud.com')) {
      adjustSelection('soundcloud');
      setupSoundcloud(url, this);
    }
    else if (bitbucket_integration_enabled && (url.attr('host') === 'bitbucket.org' || url.attr('host') === 'www.bitbucket.org')) {
      adjustSelection('bitbucket');
      setupBitbucket(url, this);
    }
    else if(this.id === 'foursquare-link' && foursquare_integration_enabled) {
      adjustSelection('foursquare');
      setupFoursquare(this);
    }
    else if(this.id === 'tent-link' && tent_integration_enabled) {
      adjustSelection('tent');
      setupTent(this);
    }
    else {
      window.location = this.href;
    }
    */
  });
},

adjustSelection = function(component) {
  var panel;
  //$('.modal-backdrop').hide();

  for (p in panels) {
    if (p !== component) {
      panel = panels[p];
      panel.hide();
    }
  }

  $('.main-nav').children('li').removeClass('sel');
  $('#' + component + '-link').parent().addClass('sel');

  currSelection = component;
};
