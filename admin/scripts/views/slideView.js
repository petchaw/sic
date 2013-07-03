define([
	'backbone',
	'collections/story'
], function(Backbone, Story){

	var SlideView = Backbone.View.extend({
		id: 'story',

		tagname: 'div',

		template: _.template('<div class="story-item"><a><%= title %> </a><p>tags: <%= tags %></p></div>'),

		initialize: function(){
			this.render();
		},


		render: function(){
			this.$el.html(this.template(this.model.toJSON()));
			return this;
		}
	});

	return SlideView;

});

