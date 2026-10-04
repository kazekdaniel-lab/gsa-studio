
// ── odsloniecie tresci przy wejsciu w kadr
const io=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.04,rootMargin:'0px 0px -6%'});
document.querySelectorAll('.cut').forEach(el=>io.observe(el));

// ── panel menu ustawiany pod paskiem, bo pasek nie ma stalej wysokosci
(function(){
  const b=document.getElementById('menuBtn'), m=document.getElementById('menu'), h=document.querySelector('header');
  if(!b||!m||!h) return;
  const pozycjonuj=()=>{m.style.top=h.getBoundingClientRect().height+'px'};
  const zamknij=()=>{m.classList.remove('otw');b.setAttribute('aria-expanded','false');b.textContent='Menu'};
  pozycjonuj(); addEventListener('resize',pozycjonuj,{passive:true});
  b.addEventListener('click',()=>{
    pozycjonuj();
    const otwarte=m.classList.toggle('otw');
    b.setAttribute('aria-expanded',String(otwarte));
    b.textContent=otwarte?'Zamknij':'Menu';
  });
  m.querySelectorAll('a').forEach(a=>a.addEventListener('click',zamknij));
  addEventListener('keydown',e=>{if(e.key==='Escape'&&m.classList.contains('otw')){zamknij();b.focus()}});
  matchMedia('(min-width:1001px)').addEventListener('change',zamknij);
})();

// ── pas kadrow: przeciaganie i postep
(function(){
  const strip=document.getElementById('strip');
  if(!strip) return;
  let down=false,sx=0,sl=0;
  strip.addEventListener('pointerdown',e=>{down=true;sx=e.clientX;sl=strip.scrollLeft;strip.classList.add('drag');strip.setPointerCapture(e.pointerId)});
  strip.addEventListener('pointermove',e=>{if(down)strip.scrollLeft=sl-(e.clientX-sx)});
  strip.addEventListener('pointerup',()=>{down=false;strip.classList.remove('drag')});
  const bar=document.querySelector('.progress .track i'), cnt=document.querySelector('.progress .mono span');
  const ile=strip.querySelectorAll('figure').length||1;
  if(!bar||!cnt) return;
  cnt.textContent='01 / '+String(ile).padStart(2,'0');
  strip.addEventListener('scroll',()=>{
    const max=strip.scrollWidth-strip.clientWidth;
    const p=max>0?strip.scrollLeft/max:0;
    bar.style.width=(18+p*82)+'%';
    cnt.textContent=String(Math.min(ile,Math.round(p*(ile-1))+1)).padStart(2,'0')+' / '+String(ile).padStart(2,'0');
  },{passive:true});
})();

// ── formularz zgloszeniowy (prototyp, bez wysylki)
(function(){
  const f=document.getElementById('zgloszenie'), stan=document.getElementById('stan');
  if(!f||!stan) return;
  f.addEventListener('submit',e=>{
    e.preventDefault();
    stan.textContent='Przyjęte. Odezwiemy się z terminem rozmowy.';
    stan.style.color='var(--znak-jasny)';
  });
})();
