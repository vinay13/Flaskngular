var app = angular.module('app', ['ui.router']);

app.config(function($stateProvider,$urlRouterProvider){

	$urlRouterProvider.otherwise("/home");


	$stateProvider
	  .state('home',{
	  	url:"/home",
	  	templateUrl:"home.html",
	  	controller: "homeCtrl"
	})
	  .state('blog',{
	  	url:"/blog",
	  	templateUrl:"blog.html",
	  	controller: "blogCtrl"

	  })
	  .state('about',{
	  	url:"/about",
	  	templateUrl : "about.html"

	  });

});


app.controller("homeCtrl",function($scope,$http){

	$http.get("http://flaskblogger.pythonanywhere.com/blogs")
	.then(function(response) {
        $scope.records = response.data.blog;
        console.log($scope.records);
    });
    });


app.controller("blogCtrl",function($scope,$http){

	$scope.read = function(p){
	var id= p; 
	$http.get("http://flaskblogger.pythonanywhere.com/blogs/" + id)
	.then(function(response) {
        $scope.records = response.data;
        console.log($scope.records);
    }); 
	};
    });


