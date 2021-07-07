var express = require('express');
var router = express.Router();

// axios を require してインスタンスを生成する
const axiosBase = require('axios');
const axios = axiosBase.create({
  baseURL: 'http://localhost:8080/backend/user_id/{user_name}', // バックエンドB のURL:port を指定する
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
  },
  responseType: 'json'
});

// [1] フロントエンドからのリクエストを受け付けて
router.get('/', function(req, res, next) {

  // [2] バックエンドB に対してリクエストを投げる
  axios.get("http://localhost:8080/backend/user_id/{user_name}")
  .then(function(response) {

    // [4] フロントエンドに対してレスポンスを返す
    res.render('chart_prc.html', response.data);
  })
  .catch(function(error) {
    console.log('ERROR!! occurred in Backend.')
  });
});

module.exports = router;
