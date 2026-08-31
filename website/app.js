console.log("KV-14 website loaded");
// Swarm animation placeholder
document.querySelectorAll(".card").forEach((c,i)=>{
  c.style.animationDelay = (i*80)+"ms";
  c.animate([{opacity:0,transform:"translateY(8px)"},{opacity:1,transform:"translateY(0)"}],{duration:500,delay:i*80,fill:"forwards"})
});
