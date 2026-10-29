document.documentElement.classList.add('js');
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
if (menu && nav) {
  menu.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
  nav.addEventListener('click', e => { if(e.target.closest('a')) {menu.setAttribute('aria-expanded','false'); nav.classList.remove('open');} });
  document.addEventListener('keydown', e => {if(e.key==='Escape'){menu.setAttribute('aria-expanded','false');nav.classList.remove('open');}});
}
const filters = [...document.querySelectorAll('.filter[data-year]')];
const search = document.querySelector('#paper-search');
const papers = [...document.querySelectorAll('[data-paper]')];
let activeYear = 'all';
function applyFilters() {
 const query = (search?.value || '').toLowerCase().trim(); let count = 0;
 papers.forEach(p => {const shown = (activeYear==='all'||p.dataset.year===activeYear) && p.textContent.toLowerCase().includes(query);p.hidden=!shown;if(shown)count++;});
 const empty=document.querySelector('#no-results'); if(empty)empty.hidden=count!==0;
 const status=document.querySelector('#search-status');if(status)status.textContent=`${count} work${count===1?' item':' items'} shown`;
}
filters.forEach(b=>b.addEventListener('click',()=>{activeYear=b.dataset.year;filters.forEach(f=>f.setAttribute('aria-pressed',String(f===b)));applyFilters();}));
search?.addEventListener('input',applyFilters);
document.querySelectorAll('[data-copy-citation]').forEach(b=>b.addEventListener('click',async()=>{const citation=document.getElementById(b.dataset.copyCitation); try {await navigator.clipboard.writeText(citation.textContent); b.textContent='Copied ✓';setTimeout(()=>{b.textContent='Copy BibTeX';},1800);}catch{citation.closest('details').open=true;const s=window.getSelection();s.removeAllRanges();const r=document.createRange();r.selectNodeContents(citation);s.addRange(r);b.textContent='Select & copy below';}}));
document.querySelector('[data-print]')?.addEventListener('click',()=>window.print());
