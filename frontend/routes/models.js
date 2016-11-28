var express = require('express');
var router = express.Router();
var api = require('../util/api.js');

/* GET specific model */
router.get('/:id', function(req, res, next) {
  var modelId = req.params.id;
  api.getModel(modelId, function(response) {
    res.render('model', {
      title: 'Model',
      path: ' > Model',
      menu: false,
      models: [response]
    });
  });
})


module.exports = router;
