define([
	'backbone',
	'underscore'
], function(Backbone, _){

	var StoryListItemView = Backbone.View.extend({

		tagName: 'li',

		template: _.template('<div class="story-item"><a><%= title %> by <%= author %></a><p> tags: <%= tags %></p></div>'),


		initialize: function(){
			this.model.bind("change", this.render, this);
			this.model.bind("destroy", this.close, this);
		},

		render: function(){
			this.$el.html(this.template(this.model.toJSON()));
			return this;
		}
	});

	return StoryListItemView;

});