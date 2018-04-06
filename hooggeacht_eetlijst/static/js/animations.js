$(document).ready(function(){

var animation = bodymovin.loadAnimation({
  container: document.getElementById('bm'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: '../static/json/construction_site.json'
})

var animation = bodymovin.loadAnimation({
  container: document.getElementById('ice'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: '../static/json/animation-w800-h600.json'
})

})
