define([
	'backbone',
	'models/slide'
], function(Backbone, Slide){
	//a batch is defined as the group of screenshots taken in the same cron job
	var Story = Backbone.Collection.extend({
		model: Slide,
		urlRoot: '/story/_id',// TODO not sure if this is right

	});

	return Story;
});
