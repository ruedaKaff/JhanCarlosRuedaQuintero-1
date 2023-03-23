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
};

export default {
  header
};
