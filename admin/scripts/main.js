requirejs.config({
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],

            exports: 'Backbone'
        },
        'underscore' : {
            exports: '_'
        },
        'jquery': {
            exports: 'jquery'
        }
    },
    paths: {
        'backbone': 'lib/backbone',
        'underscore': 'lib/underscore',
        'jquery': 'lib/jquery'
    }
})

requirejs(['collections/stories', 'collections/story', 'models/story', 'models/slide', 'views/slideView', 'views/storylist', 'views/storyListItem','views/storyView' ],
function(StoriesCollection, StoryCollection, StoryModel, SlideModel, SlideView, StoryListView, StoryListItemView, StoryView){
    var AppRouter = Backbone.Router.extend({
        routes: {
            "" : "home",
            "story/:id": "story"
        },

        // initialize: function(){
            
        // },

        home: function(){
            var storiesCollection = new StoriesCollection();
            storiesCollection.fetch({
                error: function(collection, response){
                    console.log('error', response);
                },

                success: function(collection, response){
                    for(var r = 0, l = response.length; r<l; r++){
                        var m = new StoryModel(response[r]);
                        storiesCollection.add(m);
                    }
                    var storyList = new StoryListView({collection: storiesCollection});
                }
            });
            
        }
    });
    app = new AppRouter();
    Backbone.history.start();
});