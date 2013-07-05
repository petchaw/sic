define([
	'backbone',
	'views/slideView',
	'collections/story'
], function(Backbone, SlideView, Story){

	var StoryListView = Backbone.View.extend({
		id: 'story',

		tagname: 'ul',

		initialize: function(){
			this.render();
		},


		render: function(){
			var slides = this.collection.models;
			var l = slides.length;
			for(var i = 0; i< l; i++){
				var sc = new SlideView({model: slides[i]}).render();
				this.$el.append(sc.el);
			}
			console.log(this);
			$("#content").html(this.el);
			return this;
		}
	});

	return StoryListView;

});

