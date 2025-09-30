(function () {
  function encode(s) { return encodeURIComponent(s); }

  function getPagePath() {
    // mkdocs material exposes location.pathname; keep it simple
    return window.location.pathname + window.location.hash;
  }

  function getSelectionText() {
    var sel = window.getSelection();
    return sel && sel.toString() ? sel.toString() : "";
  }

  function buildIssueUrl() {
    var repo = "OpenTraceLab/website";   // change if you want issues elsewhere
    var title = "Docs feedback: " + document.title.replace(/\s*\|\s*OpenTraceLab.*/i, "");
    var selection = getSelectionText();

    var body =
      "**Page:** " + getPagePath() + "\n\n" +
      (selection
        ? "**Selection:**\n```\n" + selection + "\n```\n\n"
        : "") +
      "**Describe the issue:**\n\n";

    // GitHub new-issue URL (uses default template chooser or blank)
    return "https://github.com/" + repo + "/issues/new" +
           "?title=" + encode(title) +
           "&body=" + encode(body);
  }

  function openIssue() {
    window.open(buildIssueUrl(), "_blank", "noopener,noreferrer");
  }

  function init() {
    var btn = document.getElementById("otl-report-issue");
    if (btn) btn.addEventListener("click", openIssue);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
