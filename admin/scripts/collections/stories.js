define([
	'backbone',
	'models/story'
], function(Backbone, Story){
	//a batch is defined as the group of screenshots taken in the same cron job
	var Stories = Backbone.Collection.extend({
		model: Story,
		url: '/story',

	});

	return Stories;
});
