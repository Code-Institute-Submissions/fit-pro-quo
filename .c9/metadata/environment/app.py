{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":53,"column":35},"end":{"row":53,"column":36},"action":"remove","lines":["."],"id":784}],[{"start":{"row":53,"column":34},"end":{"row":53,"column":35},"action":"insert","lines":["."],"id":785}],[{"start":{"row":53,"column":34},"end":{"row":53,"column":35},"action":"remove","lines":["."],"id":786}],[{"start":{"row":71,"column":38},"end":{"row":72,"column":0},"action":"insert","lines":["",""],"id":787},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]},{"start":{"row":72,"column":4},"end":{"row":73,"column":0},"action":"insert","lines":["",""]},{"start":{"row":73,"column":0},"end":{"row":73,"column":4},"action":"insert","lines":["    "]},{"start":{"row":73,"column":4},"end":{"row":74,"column":0},"action":"insert","lines":["",""]},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]},{"start":{"row":74,"column":4},"end":{"row":75,"column":0},"action":"insert","lines":["",""]},{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"insert","lines":["    "]},{"start":{"row":75,"column":4},"end":{"row":76,"column":0},"action":"insert","lines":["",""]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"remove","lines":["    "],"id":788}],[{"start":{"row":76,"column":0},"end":{"row":84,"column":41},"action":"insert","lines":["@app.route('/addexercise')","def addexercise():","    return render_template('addexercise.html', action=mongo.db.action.find())","","@app.route('/insert_exercise', methods=['POST'])","def insert_exercise():","    action_tracker = mongo.db.action_tracker","    action_tracker.insert_one(request.form.to_dict())","    return redirect(url_for('fit_track'))"],"id":789}],[{"start":{"row":64,"column":50},"end":{"row":64,"column":51},"action":"insert","lines":["_"],"id":790},{"start":{"row":64,"column":51},"end":{"row":64,"column":52},"action":"insert","lines":["n"]},{"start":{"row":64,"column":52},"end":{"row":64,"column":53},"action":"insert","lines":["a"]},{"start":{"row":64,"column":53},"end":{"row":64,"column":54},"action":"insert","lines":["m"]},{"start":{"row":64,"column":54},"end":{"row":64,"column":55},"action":"insert","lines":["e"]}],[{"start":{"row":68,"column":10},"end":{"row":68,"column":11},"action":"insert","lines":["_"],"id":791},{"start":{"row":68,"column":11},"end":{"row":68,"column":12},"action":"insert","lines":["n"]},{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["a"]},{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":["m"]},{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":10},"end":{"row":70,"column":11},"action":"insert","lines":["_"],"id":792},{"start":{"row":70,"column":11},"end":{"row":70,"column":12},"action":"insert","lines":["n"]},{"start":{"row":70,"column":12},"end":{"row":70,"column":13},"action":"insert","lines":["a"]},{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["m"]},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":73,"column":0},"end":{"row":84,"column":41},"action":"remove","lines":["    ","    ","    ","@app.route('/addexercise')","def addexercise():","    return render_template('addexercise.html', action=mongo.db.action.find())","","@app.route('/insert_exercise', methods=['POST'])","def insert_exercise():","    action_tracker = mongo.db.action_tracker","    action_tracker.insert_one(request.form.to_dict())","    return redirect(url_for('fit_track'))"],"id":793},{"start":{"row":72,"column":4},"end":{"row":73,"column":0},"action":"remove","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "]},{"start":{"row":71,"column":38},"end":{"row":72,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":64,"column":50},"end":{"row":64,"column":55},"action":"remove","lines":["_name"],"id":794}],[{"start":{"row":68,"column":10},"end":{"row":68,"column":15},"action":"remove","lines":["_name"],"id":795}],[{"start":{"row":70,"column":10},"end":{"row":70,"column":15},"action":"remove","lines":["_name"],"id":796}],[{"start":{"row":69,"column":49},"end":{"row":69,"column":50},"action":"remove","lines":["["],"id":797}],[{"start":{"row":69,"column":49},"end":{"row":69,"column":50},"action":"insert","lines":["("],"id":798}],[{"start":{"row":69,"column":63},"end":{"row":69,"column":64},"action":"remove","lines":["]"],"id":799}],[{"start":{"row":69,"column":63},"end":{"row":69,"column":64},"action":"insert","lines":[")"],"id":800}],[{"start":{"row":70,"column":4},"end":{"row":70,"column":33},"action":"remove","lines":["action.insert_one(action_doc)"],"id":801},{"start":{"row":70,"column":4},"end":{"row":70,"column":5},"action":"insert","lines":["m"]},{"start":{"row":70,"column":5},"end":{"row":70,"column":6},"action":"insert","lines":["o"]},{"start":{"row":70,"column":6},"end":{"row":70,"column":7},"action":"insert","lines":["n"]},{"start":{"row":70,"column":7},"end":{"row":70,"column":8},"action":"insert","lines":["g"]},{"start":{"row":70,"column":8},"end":{"row":70,"column":9},"action":"insert","lines":["o"]},{"start":{"row":70,"column":9},"end":{"row":70,"column":10},"action":"insert","lines":["."]},{"start":{"row":70,"column":10},"end":{"row":70,"column":11},"action":"insert","lines":["d"]},{"start":{"row":70,"column":11},"end":{"row":70,"column":12},"action":"insert","lines":["b"]}],[{"start":{"row":70,"column":12},"end":{"row":70,"column":13},"action":"insert","lines":["."],"id":802},{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["a"]},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["c"]},{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["i"],"id":803},{"start":{"row":70,"column":17},"end":{"row":70,"column":18},"action":"insert","lines":["o"]},{"start":{"row":70,"column":18},"end":{"row":70,"column":19},"action":"insert","lines":["n"]},{"start":{"row":70,"column":19},"end":{"row":70,"column":20},"action":"insert","lines":["."]}],[{"start":{"row":70,"column":20},"end":{"row":70,"column":21},"action":"insert","lines":["i"],"id":804},{"start":{"row":70,"column":21},"end":{"row":70,"column":22},"action":"insert","lines":["n"]},{"start":{"row":70,"column":22},"end":{"row":70,"column":23},"action":"insert","lines":["s"]},{"start":{"row":70,"column":23},"end":{"row":70,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":24},"end":{"row":70,"column":25},"action":"insert","lines":["r"],"id":805},{"start":{"row":70,"column":25},"end":{"row":70,"column":26},"action":"insert","lines":["t"]},{"start":{"row":70,"column":26},"end":{"row":70,"column":27},"action":"insert","lines":["_"]},{"start":{"row":70,"column":27},"end":{"row":70,"column":28},"action":"insert","lines":["o"]},{"start":{"row":70,"column":28},"end":{"row":70,"column":29},"action":"insert","lines":["n"]},{"start":{"row":70,"column":29},"end":{"row":70,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":30},"end":{"row":70,"column":32},"action":"insert","lines":["()"],"id":806}],[{"start":{"row":70,"column":31},"end":{"row":70,"column":32},"action":"insert","lines":["a"],"id":807},{"start":{"row":70,"column":32},"end":{"row":70,"column":33},"action":"insert","lines":["c"]},{"start":{"row":70,"column":33},"end":{"row":70,"column":34},"action":"insert","lines":["r"]},{"start":{"row":70,"column":34},"end":{"row":70,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":70,"column":34},"end":{"row":70,"column":35},"action":"remove","lines":["t"],"id":808},{"start":{"row":70,"column":33},"end":{"row":70,"column":34},"action":"remove","lines":["r"]}],[{"start":{"row":70,"column":33},"end":{"row":70,"column":34},"action":"insert","lines":["t"],"id":809},{"start":{"row":70,"column":34},"end":{"row":70,"column":35},"action":"insert","lines":["i"]},{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"insert","lines":["o"]},{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"insert","lines":["n"]},{"start":{"row":70,"column":37},"end":{"row":70,"column":38},"action":"insert","lines":["_"]},{"start":{"row":70,"column":38},"end":{"row":70,"column":39},"action":"insert","lines":["d"]},{"start":{"row":70,"column":39},"end":{"row":70,"column":40},"action":"insert","lines":["o"]},{"start":{"row":70,"column":40},"end":{"row":70,"column":41},"action":"insert","lines":["c"]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":28},"action":"remove","lines":["    action = mongo.db.action"],"id":810},{"start":{"row":67,"column":19},"end":{"row":68,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":70,"column":38},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":811},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]},{"start":{"row":71,"column":4},"end":{"row":72,"column":0},"action":"insert","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "],"id":812}],[{"start":{"row":72,"column":0},"end":{"row":72,"column":1},"action":"insert","lines":["@"],"id":813},{"start":{"row":72,"column":1},"end":{"row":72,"column":2},"action":"insert","lines":["a"]},{"start":{"row":72,"column":2},"end":{"row":72,"column":3},"action":"insert","lines":["p"]},{"start":{"row":72,"column":3},"end":{"row":72,"column":4},"action":"insert","lines":["p"]},{"start":{"row":72,"column":4},"end":{"row":72,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":72,"column":5},"end":{"row":72,"column":6},"action":"insert","lines":["r"],"id":814},{"start":{"row":72,"column":6},"end":{"row":72,"column":7},"action":"insert","lines":["o"]},{"start":{"row":72,"column":7},"end":{"row":72,"column":8},"action":"insert","lines":["u"]},{"start":{"row":72,"column":8},"end":{"row":72,"column":9},"action":"insert","lines":["t"]},{"start":{"row":72,"column":9},"end":{"row":72,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":72,"column":10},"end":{"row":72,"column":12},"action":"insert","lines":["()"],"id":815}],[{"start":{"row":72,"column":11},"end":{"row":72,"column":13},"action":"insert","lines":["''"],"id":816}],[{"start":{"row":72,"column":12},"end":{"row":72,"column":13},"action":"insert","lines":["d"],"id":817},{"start":{"row":72,"column":13},"end":{"row":72,"column":14},"action":"insert","lines":["e"]},{"start":{"row":72,"column":14},"end":{"row":72,"column":15},"action":"insert","lines":["l"]},{"start":{"row":72,"column":15},"end":{"row":72,"column":16},"action":"insert","lines":["e"]},{"start":{"row":72,"column":16},"end":{"row":72,"column":17},"action":"insert","lines":["t"]},{"start":{"row":72,"column":17},"end":{"row":72,"column":18},"action":"insert","lines":["e"]},{"start":{"row":72,"column":18},"end":{"row":72,"column":19},"action":"insert","lines":["_"]},{"start":{"row":72,"column":19},"end":{"row":72,"column":20},"action":"insert","lines":["s"]},{"start":{"row":72,"column":20},"end":{"row":72,"column":21},"action":"insert","lines":["p"]}],[{"start":{"row":72,"column":21},"end":{"row":72,"column":22},"action":"insert","lines":["o"],"id":818},{"start":{"row":72,"column":22},"end":{"row":72,"column":23},"action":"insert","lines":["r"]},{"start":{"row":72,"column":23},"end":{"row":72,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"insert","lines":[","],"id":819}],[{"start":{"row":72,"column":26},"end":{"row":72,"column":27},"action":"insert","lines":[" "],"id":820},{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"insert","lines":["m"]},{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"insert","lines":["e"]},{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"insert","lines":["t"]},{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"insert","lines":["h"]},{"start":{"row":72,"column":31},"end":{"row":72,"column":32},"action":"insert","lines":["o"]},{"start":{"row":72,"column":32},"end":{"row":72,"column":33},"action":"insert","lines":["d"]}],[{"start":{"row":72,"column":32},"end":{"row":72,"column":33},"action":"remove","lines":["d"],"id":821},{"start":{"row":72,"column":31},"end":{"row":72,"column":32},"action":"remove","lines":["o"]},{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"remove","lines":["h"]},{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"remove","lines":["t"]},{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"remove","lines":["e"]},{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"remove","lines":["m"]},{"start":{"row":72,"column":26},"end":{"row":72,"column":27},"action":"remove","lines":[" "]}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"remove","lines":[","],"id":822}],[{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"remove","lines":["'"],"id":823}],[{"start":{"row":72,"column":24},"end":{"row":72,"column":25},"action":"insert","lines":["/"],"id":824}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"insert","lines":["<"],"id":825}],[{"start":{"row":72,"column":26},"end":{"row":72,"column":27},"action":"insert","lines":["s"],"id":826},{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"insert","lines":["p"]},{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"insert","lines":["o"]}],[{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"insert","lines":["r"],"id":827},{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":72,"column":31},"end":{"row":72,"column":32},"action":"insert","lines":["_"],"id":828},{"start":{"row":72,"column":32},"end":{"row":72,"column":33},"action":"insert","lines":["i"]},{"start":{"row":72,"column":33},"end":{"row":72,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":72,"column":34},"end":{"row":72,"column":35},"action":"insert","lines":[">"],"id":829},{"start":{"row":72,"column":35},"end":{"row":72,"column":36},"action":"insert","lines":["'"]}],[{"start":{"row":72,"column":37},"end":{"row":73,"column":0},"action":"insert","lines":["",""],"id":830},{"start":{"row":73,"column":0},"end":{"row":73,"column":1},"action":"insert","lines":["d"]}],[{"start":{"row":73,"column":1},"end":{"row":73,"column":2},"action":"insert","lines":["e"],"id":831},{"start":{"row":73,"column":2},"end":{"row":73,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":73,"column":3},"end":{"row":73,"column":4},"action":"insert","lines":[" "],"id":832},{"start":{"row":73,"column":4},"end":{"row":73,"column":5},"action":"insert","lines":["d"]}],[{"start":{"row":73,"column":5},"end":{"row":73,"column":6},"action":"insert","lines":["e"],"id":833},{"start":{"row":73,"column":6},"end":{"row":73,"column":7},"action":"insert","lines":["l"]}],[{"start":{"row":73,"column":4},"end":{"row":73,"column":7},"action":"remove","lines":["del"],"id":834},{"start":{"row":73,"column":4},"end":{"row":73,"column":16},"action":"insert","lines":["delete_sport"]}],[{"start":{"row":73,"column":16},"end":{"row":73,"column":18},"action":"insert","lines":["()"],"id":835}],[{"start":{"row":73,"column":17},"end":{"row":73,"column":18},"action":"insert","lines":["s"],"id":836},{"start":{"row":73,"column":18},"end":{"row":73,"column":19},"action":"insert","lines":["p"]},{"start":{"row":73,"column":19},"end":{"row":73,"column":20},"action":"insert","lines":["o"]},{"start":{"row":73,"column":20},"end":{"row":73,"column":21},"action":"insert","lines":["r"]},{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"insert","lines":["t"]},{"start":{"row":73,"column":22},"end":{"row":73,"column":23},"action":"insert","lines":["_"]},{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"insert","lines":["i"]}],[{"start":{"row":73,"column":24},"end":{"row":73,"column":25},"action":"insert","lines":["d"],"id":837}],[{"start":{"row":73,"column":26},"end":{"row":73,"column":27},"action":"insert","lines":[":"],"id":838}],[{"start":{"row":73,"column":27},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":839},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":74,"column":4},"end":{"row":74,"column":5},"action":"insert","lines":["m"],"id":840},{"start":{"row":74,"column":5},"end":{"row":74,"column":6},"action":"insert","lines":["o"]},{"start":{"row":74,"column":6},"end":{"row":74,"column":7},"action":"insert","lines":["n"]},{"start":{"row":74,"column":7},"end":{"row":74,"column":8},"action":"insert","lines":["g"]},{"start":{"row":74,"column":8},"end":{"row":74,"column":9},"action":"insert","lines":["o"]},{"start":{"row":74,"column":9},"end":{"row":74,"column":10},"action":"insert","lines":["."]}],[{"start":{"row":74,"column":10},"end":{"row":74,"column":11},"action":"insert","lines":["d"],"id":841},{"start":{"row":74,"column":11},"end":{"row":74,"column":12},"action":"insert","lines":["b"]},{"start":{"row":74,"column":12},"end":{"row":74,"column":13},"action":"insert","lines":["."]},{"start":{"row":74,"column":13},"end":{"row":74,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":74,"column":14},"end":{"row":74,"column":15},"action":"insert","lines":["c"],"id":842},{"start":{"row":74,"column":15},"end":{"row":74,"column":16},"action":"insert","lines":["t"]},{"start":{"row":74,"column":16},"end":{"row":74,"column":17},"action":"insert","lines":["i"]},{"start":{"row":74,"column":17},"end":{"row":74,"column":18},"action":"insert","lines":["o"]},{"start":{"row":74,"column":18},"end":{"row":74,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":74,"column":19},"end":{"row":74,"column":20},"action":"insert","lines":["."],"id":843},{"start":{"row":74,"column":20},"end":{"row":74,"column":21},"action":"insert","lines":["r"]},{"start":{"row":74,"column":21},"end":{"row":74,"column":22},"action":"insert","lines":["e"]},{"start":{"row":74,"column":22},"end":{"row":74,"column":23},"action":"insert","lines":["m"]},{"start":{"row":74,"column":23},"end":{"row":74,"column":24},"action":"insert","lines":["o"]},{"start":{"row":74,"column":24},"end":{"row":74,"column":25},"action":"insert","lines":["v"]},{"start":{"row":74,"column":25},"end":{"row":74,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":74,"column":26},"end":{"row":74,"column":28},"action":"insert","lines":["()"],"id":844}],[{"start":{"row":74,"column":27},"end":{"row":74,"column":29},"action":"insert","lines":["{}"],"id":845}],[{"start":{"row":74,"column":28},"end":{"row":74,"column":30},"action":"insert","lines":["''"],"id":846}],[{"start":{"row":74,"column":29},"end":{"row":74,"column":30},"action":"insert","lines":["i"],"id":847}],[{"start":{"row":74,"column":30},"end":{"row":74,"column":31},"action":"insert","lines":["_"],"id":848},{"start":{"row":74,"column":31},"end":{"row":74,"column":32},"action":"insert","lines":["i"]},{"start":{"row":74,"column":32},"end":{"row":74,"column":33},"action":"insert","lines":["d"]}],[{"start":{"row":74,"column":32},"end":{"row":74,"column":33},"action":"remove","lines":["d"],"id":849},{"start":{"row":74,"column":31},"end":{"row":74,"column":32},"action":"remove","lines":["i"]},{"start":{"row":74,"column":30},"end":{"row":74,"column":31},"action":"remove","lines":["_"]},{"start":{"row":74,"column":29},"end":{"row":74,"column":30},"action":"remove","lines":["i"]}],[{"start":{"row":74,"column":29},"end":{"row":74,"column":30},"action":"insert","lines":["_"],"id":850},{"start":{"row":74,"column":30},"end":{"row":74,"column":31},"action":"insert","lines":["i"]},{"start":{"row":74,"column":31},"end":{"row":74,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":74,"column":33},"end":{"row":74,"column":34},"action":"insert","lines":[":"],"id":851}],[{"start":{"row":74,"column":34},"end":{"row":74,"column":35},"action":"insert","lines":["O"],"id":852},{"start":{"row":74,"column":35},"end":{"row":74,"column":36},"action":"insert","lines":["b"]},{"start":{"row":74,"column":36},"end":{"row":74,"column":37},"action":"insert","lines":["j"]},{"start":{"row":74,"column":37},"end":{"row":74,"column":38},"action":"insert","lines":["e"]},{"start":{"row":74,"column":38},"end":{"row":74,"column":39},"action":"insert","lines":["c"]},{"start":{"row":74,"column":39},"end":{"row":74,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":74,"column":40},"end":{"row":74,"column":41},"action":"insert","lines":["I"],"id":853},{"start":{"row":74,"column":41},"end":{"row":74,"column":42},"action":"insert","lines":["D"]}],[{"start":{"row":74,"column":42},"end":{"row":74,"column":44},"action":"insert","lines":["()"],"id":854}],[{"start":{"row":74,"column":43},"end":{"row":74,"column":44},"action":"insert","lines":["s"],"id":855},{"start":{"row":74,"column":44},"end":{"row":74,"column":45},"action":"insert","lines":["p"]},{"start":{"row":74,"column":45},"end":{"row":74,"column":46},"action":"insert","lines":["o"]},{"start":{"row":74,"column":46},"end":{"row":74,"column":47},"action":"insert","lines":["r"]},{"start":{"row":74,"column":47},"end":{"row":74,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":74,"column":48},"end":{"row":74,"column":49},"action":"insert","lines":["_"],"id":856},{"start":{"row":74,"column":49},"end":{"row":74,"column":50},"action":"insert","lines":["n"]},{"start":{"row":74,"column":50},"end":{"row":74,"column":51},"action":"insert","lines":["a"]}],[{"start":{"row":74,"column":50},"end":{"row":74,"column":51},"action":"remove","lines":["a"],"id":857},{"start":{"row":74,"column":49},"end":{"row":74,"column":50},"action":"remove","lines":["n"]}],[{"start":{"row":74,"column":49},"end":{"row":74,"column":50},"action":"insert","lines":["i"],"id":858},{"start":{"row":74,"column":50},"end":{"row":74,"column":51},"action":"insert","lines":["d"]}],[{"start":{"row":74,"column":54},"end":{"row":75,"column":0},"action":"insert","lines":["",""],"id":859},{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"insert","lines":["    "]},{"start":{"row":75,"column":4},"end":{"row":75,"column":5},"action":"insert","lines":["r"]},{"start":{"row":75,"column":5},"end":{"row":75,"column":6},"action":"insert","lines":["e"]},{"start":{"row":75,"column":6},"end":{"row":75,"column":7},"action":"insert","lines":["t"]},{"start":{"row":75,"column":7},"end":{"row":75,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":75,"column":4},"end":{"row":75,"column":8},"action":"remove","lines":["retu"],"id":860},{"start":{"row":75,"column":4},"end":{"row":75,"column":10},"action":"insert","lines":["return"]}],[{"start":{"row":75,"column":10},"end":{"row":75,"column":11},"action":"insert","lines":[" "],"id":861},{"start":{"row":75,"column":11},"end":{"row":75,"column":12},"action":"insert","lines":["r"]},{"start":{"row":75,"column":12},"end":{"row":75,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":11},"end":{"row":75,"column":13},"action":"remove","lines":["re"],"id":862},{"start":{"row":75,"column":11},"end":{"row":75,"column":19},"action":"insert","lines":["redirect"]}],[{"start":{"row":75,"column":19},"end":{"row":75,"column":21},"action":"insert","lines":["()"],"id":863}],[{"start":{"row":75,"column":20},"end":{"row":75,"column":21},"action":"insert","lines":["u"],"id":864},{"start":{"row":75,"column":21},"end":{"row":75,"column":22},"action":"insert","lines":["r"]},{"start":{"row":75,"column":22},"end":{"row":75,"column":23},"action":"insert","lines":["l"]},{"start":{"row":75,"column":23},"end":{"row":75,"column":24},"action":"insert","lines":["_"]},{"start":{"row":75,"column":24},"end":{"row":75,"column":25},"action":"insert","lines":["f"]},{"start":{"row":75,"column":25},"end":{"row":75,"column":26},"action":"insert","lines":["o"]},{"start":{"row":75,"column":26},"end":{"row":75,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":75,"column":27},"end":{"row":75,"column":29},"action":"insert","lines":["()"],"id":865}],[{"start":{"row":75,"column":28},"end":{"row":75,"column":30},"action":"insert","lines":["''"],"id":866}],[{"start":{"row":75,"column":29},"end":{"row":75,"column":30},"action":"insert","lines":["s"],"id":867},{"start":{"row":75,"column":30},"end":{"row":75,"column":31},"action":"insert","lines":["p"]},{"start":{"row":75,"column":31},"end":{"row":75,"column":32},"action":"insert","lines":["o"]},{"start":{"row":75,"column":32},"end":{"row":75,"column":33},"action":"insert","lines":["r"]},{"start":{"row":75,"column":33},"end":{"row":75,"column":34},"action":"insert","lines":["t"]},{"start":{"row":75,"column":34},"end":{"row":75,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":75,"column":38},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":868},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "]},{"start":{"row":76,"column":4},"end":{"row":77,"column":0},"action":"insert","lines":["",""]},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]},{"start":{"row":77,"column":4},"end":{"row":78,"column":0},"action":"insert","lines":["",""]},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":78,"column":4},"end":{"row":78,"column":62},"action":"insert","lines":["mongo.db.categories.remove({'_id': ObjectId(category_id)})"],"id":869}],[{"start":{"row":77,"column":0},"end":{"row":78,"column":62},"action":"remove","lines":["    ","    mongo.db.categories.remove({'_id': ObjectId(category_id)})"],"id":870},{"start":{"row":76,"column":4},"end":{"row":77,"column":0},"action":"remove","lines":["",""]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":74,"column":41},"end":{"row":74,"column":42},"action":"remove","lines":["D"],"id":871}],[{"start":{"row":74,"column":41},"end":{"row":74,"column":42},"action":"insert","lines":["d"],"id":872}],[{"start":{"row":75,"column":38},"end":{"row":76,"column":0},"action":"remove","lines":["",""],"id":873}],[{"start":{"row":72,"column":12},"end":{"row":72,"column":13},"action":"insert","lines":["/"],"id":874}],[{"start":{"row":72,"column":27},"end":{"row":72,"column":32},"action":"remove","lines":["sport"],"id":875},{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"insert","lines":["a"]},{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"insert","lines":["c"]},{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"insert","lines":["t"]},{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"insert","lines":["i"]},{"start":{"row":72,"column":31},"end":{"row":72,"column":32},"action":"insert","lines":["o"]},{"start":{"row":72,"column":32},"end":{"row":72,"column":33},"action":"insert","lines":["n"]},{"start":{"row":72,"column":33},"end":{"row":72,"column":34},"action":"insert","lines":["_"]}],[{"start":{"row":72,"column":34},"end":{"row":72,"column":35},"action":"insert","lines":["n"],"id":876},{"start":{"row":72,"column":35},"end":{"row":72,"column":36},"action":"insert","lines":["a"]},{"start":{"row":72,"column":36},"end":{"row":72,"column":37},"action":"insert","lines":["m"]},{"start":{"row":72,"column":37},"end":{"row":72,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":73,"column":17},"end":{"row":73,"column":22},"action":"remove","lines":["sport"],"id":877},{"start":{"row":73,"column":17},"end":{"row":73,"column":18},"action":"insert","lines":["a"]},{"start":{"row":73,"column":18},"end":{"row":73,"column":19},"action":"insert","lines":["c"]},{"start":{"row":73,"column":19},"end":{"row":73,"column":20},"action":"insert","lines":["t"]},{"start":{"row":73,"column":20},"end":{"row":73,"column":21},"action":"insert","lines":["i"]},{"start":{"row":73,"column":21},"end":{"row":73,"column":22},"action":"insert","lines":["o"]},{"start":{"row":73,"column":22},"end":{"row":73,"column":23},"action":"insert","lines":["n"]},{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"insert","lines":["_"]}],[{"start":{"row":73,"column":24},"end":{"row":73,"column":25},"action":"remove","lines":["_"],"id":878}],[{"start":{"row":74,"column":43},"end":{"row":74,"column":48},"action":"remove","lines":["sport"],"id":879},{"start":{"row":74,"column":43},"end":{"row":74,"column":44},"action":"insert","lines":["a"]},{"start":{"row":74,"column":44},"end":{"row":74,"column":45},"action":"insert","lines":["c"]},{"start":{"row":74,"column":45},"end":{"row":74,"column":46},"action":"insert","lines":["t"]},{"start":{"row":74,"column":46},"end":{"row":74,"column":47},"action":"insert","lines":["i"]},{"start":{"row":74,"column":47},"end":{"row":74,"column":48},"action":"insert","lines":["o"]},{"start":{"row":74,"column":48},"end":{"row":74,"column":49},"action":"insert","lines":["n"]}],[{"start":{"row":74,"column":49},"end":{"row":74,"column":50},"action":"insert","lines":["_"],"id":880},{"start":{"row":74,"column":50},"end":{"row":74,"column":51},"action":"insert","lines":["n"]},{"start":{"row":74,"column":51},"end":{"row":74,"column":52},"action":"insert","lines":["a"]},{"start":{"row":74,"column":52},"end":{"row":74,"column":53},"action":"insert","lines":["m"]},{"start":{"row":74,"column":53},"end":{"row":74,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":73,"column":23},"end":{"row":73,"column":24},"action":"insert","lines":["_"],"id":881},{"start":{"row":73,"column":24},"end":{"row":73,"column":25},"action":"insert","lines":["n"]},{"start":{"row":73,"column":25},"end":{"row":73,"column":26},"action":"insert","lines":["a"]},{"start":{"row":73,"column":26},"end":{"row":73,"column":27},"action":"insert","lines":["m"]},{"start":{"row":73,"column":27},"end":{"row":73,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":72,"column":30},"end":{"row":72,"column":38},"action":"remove","lines":["ion_name"],"id":882}],[{"start":{"row":73,"column":20},"end":{"row":73,"column":28},"action":"remove","lines":["ion_name"],"id":883}],[{"start":{"row":74,"column":46},"end":{"row":74,"column":54},"action":"remove","lines":["ion_name"],"id":884}]]},"ace":{"folds":[],"scrolltop":881,"scrollleft":0,"selection":{"start":{"row":73,"column":19},"end":{"row":73,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1581681317870,"hash":"09e2314fb2ff4b4a7f83619b889be19559bc2bb7"}