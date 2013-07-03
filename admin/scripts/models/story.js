define([
	'backbone'
], function(Backbone){

	var Story = Backbone.Model.extend({
		defaults: function(){
			return {
				url: '',
				image_url: '',
				device: null,
				os: '',
				created_at: '',
				id: '',
				state: '',
				os_version: '',
				thumb_url: '',
				orientation: null,
				browser: '',
				browser_version: ''
			}; 
		},

		initialize: function(options){
			this.url = options.url;
			this.image_url = options.image_url;
			this.device = options.device;
			this.os = options.os;
			this.created_at = options.created_at;
			this.id = options.id;
			this.state = options.state;
			this.os_version = options.os_version;
			this.thumb_url = options.thumb_url;
			this.orientation = options.orientation;
			this.browser = options.browser;
			this.browser_version = options.browser_version;
		},

		idAttribute: "_id",

	});

	return Story;

});
