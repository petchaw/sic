define([
	'backbone',
	'views/storyView',
	'collections/stories'
], function(Backbone, StoryListItemView, Batch){

	var StoryListView = Backbone.View.extend({
		id: 'story',

		tagname: 'ul',

		initialize: function(){
			this.render();
		},


		render: function(){
			var stories = this.collection.models;
			var l = screenshots.length;
			for(var i = 0; i< l; i++){
				var storyListItem = new StoryListItemView({model: stories[i]}).render();
				this.$el.append(sc.el);
			}
			console.log(this);
			$("#content").html(this.el);
			return this;
		}
	});

	return StoryListView;

});

