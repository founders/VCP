$(document).ready(function() {

	$("#startupsGrid").kendoGrid({
        sortable: true,
        groupable: true,
        dataSource: {
            data: {'startups': []},
            schema: {
                data: "startups"
            }
        },
        columns: [
            {
                field: "name",
                title: "Name"
            },
        ]
    });

    $.getJSON("/data/startups/", function(startups) {
        console.log(startups);
        $("#startupsGrid").data("kendoGrid").dataSource.data(startups['startups']);
    });
});
