function plot01(id) {
            var ele = document.getElementById(id)
            var trace = []

            trace[0] = {
                x: {{ date|safe }},
                y: {{ price_close }},
                type: "scatter"
            }

            Plotly.plot(ele, trace)
        }