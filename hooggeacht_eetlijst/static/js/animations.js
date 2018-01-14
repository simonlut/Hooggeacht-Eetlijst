$(document).ready(function(){

var animation = bodymovin.loadAnimation({
  container: document.getElementById('bm'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'static/json/construction_site.json'
})

var animation2 = bodymovin.loadAnimation({
  container: document.getElementById('bp'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'static/json/construction_site.json'
})

})
