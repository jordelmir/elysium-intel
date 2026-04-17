import sqlite3
conn = sqlite3.connect("/home/ubuntu/elysium_intel_v2.db")
nodes = conn.execute("SELECT DISTINCT valor FROM entities").fetchall()
edges = conn.execute("SELECT caso_a, caso_b, vinculo FROM relations").fetchall()
with open("/home/ubuntu/elysium_forensic_graph.gexf", "w") as f:
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<gexf xmlns=\"http://www.gexf.net/1.2draft\" version=\"1.2\">\n")
    f.write("  <graph mode=\"static\" defaultedgetype=\"undirected\">\n    <nodes>\n")
    for node in nodes:
        f.write(f"      <node id=\"{node[0]}\" label=\"{node[0]}\" />\n")
    f.write("    </nodes>\n    <edges>\n")
    for i, edge in enumerate(edges):
        f.write(f"      <edge id=\"{i}\" source=\"{edge[0]}\" target=\"{edge[1]}\" label=\"{edge[2]}\" />\n")
    f.write("    </edges>\n  </graph>\n</gexf>")
conn.close()
