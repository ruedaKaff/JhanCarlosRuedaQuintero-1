let header = {
  tittle: {
    name: "TITULO llamativo",
    href: "#",
  },
  company: [
    {
      name: "ITEM1",
      href: "#",
    },
    {
      name: "ITEM2",
      href: "#",  
    },
    {
      name: "ITEM3",
      href: "#",
    },
    {
      name: "ITEM4",
      href: "#",
    },
    {
      name: "ITEM5",
      href: "#",
    },
    {
      name: "ITEM6",
      href: "#",
    },
    {
      name: "ITEM7",
      href: "#",
    },
  ],
  listCompanies() {
    let plantilla = "";
    this.company.forEach((val, id) => {
      plantilla += `<a class="p-2 link-secondary" href="${val.href}">${val.name} </a> `;
    });

    document
      .querySelector(".company")
      .insertAdjacentHTML("beforeend", plantilla);
  },

  fragShow() {
    let plantilla = "";
    for (let i = 0; 100; i++) {
      document.body.insertAdjacentHTML ("beforeend", `<h1> hola '${i} ' </h1>`)      
    }
    postMessage({mensaje: plantilla});

  /*   const ws = new Worker("storage/wsMyheader.js", {type:"module"});
    ws.postMessage({nombre : "jim"});

    ws.addEventListener("message", (e)=>{
      console.log(e.data);
      ws.terminate();
    }) */
  }
};





export default {
  header
};
