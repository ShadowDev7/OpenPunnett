let lang = "el";

const t = {
 el: {
  p1:"Γονέας 1 (π.χ. Aa / Αα)",
  p2:"Γονέας 2 (π.χ. Aa / Αα)",
  calc:"<span class='material-symbols-outlined'>science</span>Υπολογισμός",
  explain:"<span class='material-symbols-outlined'>lightbulb</span>Εξήγηση",
  export:"<span class='material-symbols-outlined'>download</span>Export",
  error:"Λάθος γονότυπος",
  validError:"Πρέπει να είναι AA, Aa, aA, aa (ή ελληνικά Α/α)",
  results:"Αποτελέσματα",
  ai:"🧠 Εξήγηση",
  histTitle:"Ιστορικό",
  histClear:"Καθαρισμός"
 },
 en: {
  p1:"Parent 1 (e.g. Aa)",  
  p2:"Parent 2 (e.g. Aa)",
  calc:"<span class='material-symbols-outlined'>science</span>Calculate",
  explain:"<span class='material-symbols-outlined'>lightbulb</span>Explain",
  export:"<span class='material-symbols-outlined'>download</span>Export",
  error:"Invalid genotype",
  validError:"Must be AA, Aa, aA, aa (or Greek Α/α)",
  results:"Results",
  ai:"🧠 Explanation",
  histTitle:"History",
  histClear:"Clear All"
 }
};

function normalizeGenotype(g){
  return g
    .replace(/Α/g, "A")
    .replace(/α/g, "a");
}

function applyLang(){
 document.getElementById("p1").placeholder = t[lang].p1;
 document.getElementById("p2").placeholder = t[lang].p2;
 
 document.getElementById("btn1").innerHTML = t[lang].calc;
 document.getElementById("btn2").innerHTML = t[lang].explain;
 document.getElementById("btn3").innerHTML = t[lang].export;

 document.getElementById("output").innerHTML="";
 document.getElementById("ai").innerHTML="";
 renderHistory(); // Dynamic translation layout catch
}

function toggleLang(){
 const thumb = document.getElementById("thumb");

 if (lang==="el"){
   lang="en";
   thumb.style.transform="translateX(38px)";
   thumb.innerText="🇬🇧";
 } else {
   lang="el";
   thumb.style.transform="translateX(0)";
   thumb.innerText="🇬🇷";
 }

 applyLang();
}

function combine(a,b){
 return (a+b).split("").sort().join("");
}

function calculate(){
 let p1 = document.getElementById("p1").value.trim();
 let p2 = document.getElementById("p2").value.trim();

 p1 = normalizeGenotype(p1);
 p2 = normalizeGenotype(p2);

 const valid = ["AA","Aa","aA","aa"];

 if(!valid.includes(p1) || !valid.includes(p2)) {
   alert(t[lang].validError);
   return;
 }

 const g1=[...p1];
 const g2=[...p2];

 let counts={};
 let html="<table><tr><th></th>";

 for(let j=0;j<g2.length;j++){
  html+=`<th>${g2[j]}</th>`;
 }
 html+="</tr>";

 for(let i=0;i<g1.length;i++){
  html+=`<tr><th>${g1[i]}</th>`;
  for(let j=0;j<g2.length;j++){
    let c=combine(g1[i],g2[j]);
    html+=`<td>${c}</td>`;
    counts[c]=(counts[c]||0)+1;
  }
  html+="</tr>";
 }

 html+="</table>";

 let total=Object.values(counts).reduce((a,b)=>a+b,0);
 let bars="<div class='bar-container'>";

 for(let k in counts){
   let p=(counts[k]/total*100);
   bars+=`<div>${k} - ${p.toFixed(0)}%</div>`;
   bars+=`<div class='bar' style='width:${p*3}px'></div>`;
 }

 bars+="</div>";

 document.getElementById("output").innerHTML =
 `<div class='result'><h3>${t[lang].results}</h3></div>` + html + bars;

 saveHistory(p1,p2);
}

function explain(){
 let p1 = document.getElementById("p1").value.trim();
 let p2 = document.getElementById("p2").value.trim();

 p1 = normalizeGenotype(p1);
 p2 = normalizeGenotype(p2);

 const valid = ["AA","Aa","aA","aa"];

 if(!valid.includes(p1) || !valid.includes(p2)){
   alert(t[lang].validError);
   return;
 }

 let meaning = {
  AA: lang==="el"?"ομόζυγος κυρίαρχος":"homozygous dominant",
  Aa: lang==="el"?"ετερόζυγος":"heterozygous",
  aA: lang==="el"?"ετερόζυγος":"heterozygous",
  aa: lang==="el"?"ομόζυγος υπολειπόμενος":"homozygous recessive"
 };

 document.getElementById("ai").innerHTML =
 `<div class="result">
   <h3>${t[lang].ai}</h3>
   <p>${p1}: ${meaning[p1]}</p>
   <p>${p2}: ${meaning[p2]}</p>
 </div>`;
}

function exportData() {
 const p1 = normalizeGenotype(document.getElementById("p1").value);
 const p2 = normalizeGenotype(document.getElementById("p2").value);

 const output = document.getElementById("output").innerText;
 const ai = document.getElementById("ai").innerText;

 let content =
 `OpenPunnett Calculator Export
-------------------
Parent 1: ${p1}
Parent 2: ${p2}

RESULTS:
${output}

EXPLANATION:
${ai}
`;

 const blob = new Blob([content], {type:"text/plain"});
 const url = URL.createObjectURL(blob);

 const a = document.createElement("a");
 a.href = url;
 a.download = "punnett-results.txt";
 a.click();

 URL.revokeObjectURL(url);
}

/* History Core State Engine */
function saveHistory(p1,p2){
 let h = JSON.parse(localStorage.getItem("h")||"[]");
 h.unshift(`${p1} × ${p2}`);
 h = h.slice(0,5);
 localStorage.setItem("h",JSON.stringify(h));
 renderHistory();
}

function renderHistory() {
 let h = JSON.parse(localStorage.getItem("h")||"[]");
 const historyDiv = document.getElementById("history");
 
 if(h.length === 0) {
   historyDiv.innerHTML = "";
   historyDiv.style.display = "none"; /* Collapses structural element footprint completely to avoid black background circle artifacts */
   return;
 }

 historyDiv.innerHTML = `
   <div class="history-title">
     <span>${t[lang].histTitle}</span>
     <button class="clear-btn" onclick="clearHistory()">
       <span class="material-symbols-outlined" style="font-size:14px">delete</span>${t[lang].histClear}
     </button>
   </div>
   <div class="history-items">${h.join("<br>")}</div>
 `;
 historyDiv.style.display = "block";
}

function clearHistory() {
 localStorage.removeItem("h");
 renderHistory();
}

window.onload = function() {
  applyLang();
  renderHistory();
};