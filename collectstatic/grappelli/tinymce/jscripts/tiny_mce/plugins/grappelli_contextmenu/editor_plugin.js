(function () {
    tinymce.PluginManager.requireLangPack("grappelli_contextmenu");
    var a = tinymce.dom.Event, c = tinymce.each, b = tinymce.DOM;
    tinymce.create("tinymce.plugins.ContextMenu", {init: function (d) {
        var f = this;
        f.editor = d;
        f.onContextMenu = new tinymce.util.Dispatcher(this);
        d.onContextMenu.add(function (g, h) {
            if (!h.ctrlKey) {
                f._getMenu(g).showMenu(h.clientX, h.clientY);
                a.add(g.getDoc(), "click", e);
                a.cancel(h)
            }
        });
        function e() {
            if (f._menu) {
                f._menu.removeAll();
                f._menu.destroy();
                a.remove(d.getDoc(), "click", e)
            }
        }

        d.onMouseDown.add(e);
        d.onKeyDown.add(e);
        d.addCommand("mcePBefore", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                new_p = d.dom.create("p", {}, "<br />");
                pe.parentNode.insertBefore(new_p, pe)
            }
        });
        d.addCommand("mcePAfter", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                new_p = d.dom.create("p", {}, "<br />");
                d.dom.insertAfter(new_p, pe)
            }
        });
        d.addCommand("mcePBeforeRoot", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                nn_p = g.parentNode.nodeName;
                if ((nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") && nn_p == "BODY") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                new_p = d.dom.create("p", {}, "<br />");
                pe.parentNode.insertBefore(new_p, pe)
            }
        });
        d.addCommand("mcePAfterRoot", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                nn_p = g.parentNode.nodeName;
                if ((nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") && nn_p == "BODY") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                new_p = d.dom.create("p", {}, "<br />");
                d.dom.insertAfter(new_p, pe)
            }
        });
        d.addCommand("mceDelete", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                d.dom.remove(pe)
            }
        });
        d.addCommand("mceDeleteRoot", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                nn_p = g.parentNode.nodeName;
                if ((nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") && nn_p == "BODY") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                d.dom.remove(pe)
            }
        });
        d.addCommand("mceMoveUp", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                pre_prev = f._getPreviousSibling(pe);
                if (pre_prev) {
                    pre_prev.parentNode.insertBefore(pe, pre_prev)
                }
            }
        });
        d.addCommand("mceMoveUpRoot", function () {
            ce = d.selection.getNode();
            pe = d.dom.getParent(ce, function (g) {
                nn = g.nodeName;
                nn_p = g.parentNode.nodeName;
                if ((nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") && nn_p == "BODY") {
                    return g
                }
            }, d.dom.getRoot());
            if (pe) {
                pre_prev = f._getPreviousSibling(pe);
                if (pre_prev) {
                    pre_prev.parentNode.insertBefore(pe, pre_prev)
                }
            }
        })
    }, getInfo: function () {
        return{longname: "Grappelli (Contextmenu)", author: "Patrick Kranzlmueller", authorurl: "http://vonautomatisch.at", infourl: "http://code.google.com/p/django-grappelli/", version: "0.1"}
    }, _getMenu: function (h) {
        var l = this, f = l._menu, i = h.selection, e = i.isCollapsed(), d = i.getNode() || h.getBody(), g, k, j;
        if (f) {
            f.removeAll();
            f.destroy()
        }
        k = b.getPos(h.getContentAreaContainer());
        j = b.getPos(h.getContainer());
        f = h.controlManager.createDropMenu("contextmenu", {offset_x: k.x + h.getParam("contextmenu_offset_x", 0), offset_y: k.y + h.getParam("contextmenu_offset_y", 0), constrain: 1});
        l._menu = f;
        pe = h.dom.getParent(d, function (m) {
            nn = m.nodeName;
            if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE") {
                return m
            }
        }, h.dom.getRoot());
        re = h.dom.getParent(d, function (m) {
            nn = m.nodeName;
            nn_p = m.parentNode.nodeName;
            if (nn == "P" || nn == "H1" || nn == "H2" || nn == "H3" || nn == "H4" || nn == "H5" || nn == "H6" || nn == "UL" || nn == "OL" || nn == "BLOCKQUOTE" && nn_p == "BODY") {
                return m
            }
        }, h.dom.getRoot());
        title_prefix = pe.nodeName;
        title_prefix_root = re.nodeName;
        title_b_before = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_insertpbefore_desc";
        title_b_after = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_insertpafter_desc";
        title_b_before_root = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_insertpbeforeroot_desc";
        title_b_after_root = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_insertpafterroot_desc";
        title_b_delete = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_delete_desc";
        title_b_delete_root = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_deleteroot_desc";
        title_b_moveup = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_moveup_desc";
        title_b_moveup_root = "grappelli_contextmenu." + title_prefix + "_grappelli_contextmenu_moveuproot_desc";
        f.add({title: title_b_before, icon: "", cmd: "mcePBefore"});
        f.add({title: title_b_after, icon: "", cmd: "mcePAfter"});
        if (pe.parentNode.nodeName != "BODY") {
            f.addSeparator();
            f.add({title: title_b_before_root, icon: "", cmd: "mcePBeforeRoot"});
            f.add({title: title_b_after_root, icon: "", cmd: "mcePAfterRoot"})
        }
        f.addSeparator();
        f.add({title: title_b_delete, icon: "", cmd: "mceDelete"});
        if (pe.parentNode.nodeName != "BODY") {
            f.add({title: title_b_delete_root, icon: "", cmd: "mceDeleteRoot"})
        }
        f.addSeparator();
        f.add({title: title_b_moveup, icon: "", cmd: "mceMoveUp"});
        if (pe.parentNode.nodeName != "BODY") {
            f.add({title: title_b_moveup_root, icon: "", cmd: "mceMoveUpRoot"})
        }
        l.onContextMenu.dispatch(l, f, d, e);
        return f
    }, _getPreviousSibling: function (e) {
        var d = e.previousSibling;
        while (d && (d.nodeType == document.TEXT_NODE || d.nodeType == document.CDATA_NODE) && d.nodeValue.match(/^\s*$/)) {
            d = d.previousSibling
        }
        return d
    }});
    tinymce.PluginManager.add("grappelli_contextmenu", tinymce.plugins.ContextMenu)
})();