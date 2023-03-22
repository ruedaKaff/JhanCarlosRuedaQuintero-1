let header = {
  tittle: {
    name: "Titulo llamativo",
    href: "#",
  },
  company: [
    {
      name: "Hola",
      href: "#",
    },
    {
      name: "Mundo",
      href: "#",
    },
    {
      name: "Mundo",
      href: "#",
    },
    {
      name: "Mundo",
      href: "#",
    },
    {
      name: "Mundo",
      href: "#",
    },
    {
      name: "Mundo",
      href: "#",
    },
    {
      name: "Mundo",
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
  header,
};
