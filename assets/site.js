
// ciecie zamiast fade-up
const io=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.05,rootMargin:'0px 0px -8%'});
document.querySelectorAll('.cut,.mask').forEach(el=>io.observe(el));

// numer sekcji przy krawedzi + metryka w pasku
const secs=[...document.querySelectorAll('section[data-num]')];
const railNum=document.getElementById('railNum'),hdMeta=document.getElementById('hdMeta');
const NAZWY={'00':'Otwarcie','01':'Materiał','02':'Rachunek godzin','03':'Przebieg','04':'Wykaz','05':'Zakres','06':'Kto to robi','07':'Studio','08':'Pytania','09':'Zgłoszenie'};
let last='';
addEventListener('scroll',()=>{
  const y=innerHeight*.42;
  let cur=secs[0];
  for(const s of secs){const r=s.getBoundingClientRect();if(r.top<=y)cur=s}
  const n=cur.dataset.num;
  if(n!==last){last=n;railNum.textContent=n;
    hdMeta.innerHTML=n==='00'?'<span>Warszawa</span><span>Produkcja wideopodcastów end-to-end</span>':'<span>'+n+'</span><span>'+NAZWY[n]+'</span>';}
},{passive:true});

// pas kadrow: przeciaganie mysza + postep
const strip=document.getElementById('strip');
let down=false,sx=0,sl=0;
strip.addEventListener('pointerdown',e=>{down=true;sx=e.clientX;sl=strip.scrollLeft;strip.classList.add('drag');strip.setPointerCapture(e.pointerId)});
strip.addEventListener('pointermove',e=>{if(down)strip.scrollLeft=sl-(e.clientX-sx)});
strip.addEventListener('pointerup',()=>{down=false;strip.classList.remove('drag')});
const bar=document.querySelector('.progress .track i'),cnt=document.querySelector('.progress .mono span');
strip.addEventListener('scroll',()=>{
  const max=strip.scrollWidth-strip.clientWidth;
  const p=max>0?strip.scrollLeft/max:0;
  bar.style.width=(18+p*82)+'%';
  cnt.textContent=String(Math.min(5,Math.round(p*4)+1)).padStart(2,'0')+' / 05';
},{passive:true});

// formularz - prototyp
document.getElementById('zgloszenie').addEventListener('submit',e=>{
  e.preventDefault();
  document.getElementById('stan').textContent='Przyjęte. Odezwiemy się z terminem rozmowy.';
  document.getElementById('stan').style.color='var(--accent)';
});
