
const language=document.documentElement.lang;
try {localStorage.setItem('zero-language',language);} catch {}
const menu=document.querySelector('.menu'),nav=document.querySelector('#navigation');
function closeMenu(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');}
menu?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});
nav?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menu.focus();}});
document.addEventListener('click',e=>{if(!e.target.closest('header'))closeMenu();});
matchMedia('(min-width:801px)').addEventListener('change',closeMenu);

// Match the visible content block, not a hash left behind by earlier navigation.
const positionKey='zero-language-position';
const blocks=[...document.querySelectorAll('main section, main .heading, .feature, .art, .font-card, .download, footer')];
const readingLine=()=>document.querySelector('header').getBoundingClientRect().height+24;
document.querySelectorAll('[data-language]').forEach(a=>a.addEventListener('click',e=>{
 if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
 if(a.dataset.language===language){e.preventDefault();return;}
 const line=readingLine();
 let index=0;
 blocks.forEach((el,i)=>{if(el.getBoundingClientRect().top<=line)index=i;});
 const block=blocks[index],rect=block.getBoundingClientRect();
 const section=block.closest('section');
 const target=new URL(a.href);
 target.hash=section?.id||'';
 a.href=target.href;
 try{
  localStorage.setItem('zero-language',a.dataset.language);
  sessionStorage.setItem(positionKey,JSON.stringify({path:target.pathname,index,progress:(line-rect.top)/Math.max(1,rect.height),top:scrollY<2}));
 }catch{}
}));
let savedPosition;
try{savedPosition=JSON.parse(sessionStorage.getItem(positionKey));sessionStorage.removeItem(positionKey);}catch{}
if(savedPosition?.path===location.pathname){
 const restore=async()=>{
  await document.fonts.ready;
  requestAnimationFrame(()=>requestAnimationFrame(()=>{
   const block=blocks[savedPosition.index];
   if(!block)return;
   const rect=block.getBoundingClientRect();
   scrollTo({top:savedPosition.top?0:scrollY+rect.top+savedPosition.progress*rect.height-readingLine(),behavior:'instant'});
  }));
 };
 if(document.readyState==='complete')restore();
 else window.addEventListener('load',restore,{once:true});
}
