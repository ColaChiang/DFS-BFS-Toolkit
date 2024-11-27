from flask import request, jsonify, render_template
from .dfs import FileSearch
from .bfs import ShortestPath

# 模擬檔案系統與圖結構
file_system = {
    "root": {"home": {"docs": ["file1.txt", "file2.txt"], "user": []}, "var": ["log.txt", "tmp.txt"], "etc": []}
}

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/file_system', methods=['GET'])
    def file_system_structure():
        return jsonify(file_system)

    @app.route('/graph', methods=['GET'])
    def graph_structure():
        return jsonify(graph)

    @app.route('/dfs_search', methods=['GET'])
    def dfs_search():
        target_file = request.args.get('file')
        searcher = FileSearch(file_system)
        result = searcher.dfs_search("root", target_file)
        return jsonify({"result": result})

    @app.route('/bfs_path', methods=['GET'])
    def bfs_path():
        start = request.args.get('start')
        end = request.args.get('end')
        path_finder = ShortestPath(graph)
        result = path_finder.bfs_shortest_path(start, end)
        return jsonify({"path": result})
