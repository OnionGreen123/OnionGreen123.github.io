const statuses=[...document.querySelectorAll('[data-status]')];
const shows=[...document.querySelectorAll('.show')];
function filterShows(status){let n=0;shows.forEach(s=>{s.hidden=status!=='all'&&!s.classList.contains(status);if(!s.hidden)n++;});statuses.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.status===status)));document.querySelector('.journal-status').textContent=`${n} live event${n===1?'':'s'} shown`;}
statuses.forEach(b=>b.addEventListener('click',()=>filterShows(b.dataset.status)));
document.querySelectorAll('.map-event').forEach(a=>a.addEventListener('click',()=>filterShows('all')));
