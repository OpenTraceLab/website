(function () {
  function normalize(s) { return (s || "").toLowerCase(); }
  function filterTable(tbl, q) {
    q = normalize(q);
    const rows = tbl.tBodies[0].rows;
    for (const tr of rows) {
      tr.style.display = normalize(tr.innerText).includes(q) ? "" : "none";
    }
  }
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".hw-filter").forEach(input => {
      const tbl = document.getElementById(input.dataset.target);
      if (tbl) input.addEventListener("input", () => filterTable(tbl, input.value));
    });
  });
})();
