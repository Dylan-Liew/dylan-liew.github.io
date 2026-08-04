(() => {
  const normalizePath = (path) => {
    const normalized = decodeURI(path)
      .replace(/index\.html$/, "")
      .replace(/\/+$/, "");

    return normalized || "/";
  };

  const updateActiveTab = () => {
    const currentPath = normalizePath(window.location.pathname);
    const links = document.querySelectorAll(".site-nav__link");

    links.forEach((link, index) => {
      const targetPath = normalizePath(new URL(link.href, window.location.href).pathname);
      const isActive = index === 0
        ? currentPath === targetPath
        : currentPath === targetPath || currentPath.startsWith(`${targetPath}/`);

      link.classList.toggle("site-nav__link--active", isActive);

      if (isActive) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(updateActiveTab);
  } else {
    document.addEventListener("DOMContentLoaded", updateActiveTab);
    window.addEventListener("popstate", updateActiveTab);
  }
})();
