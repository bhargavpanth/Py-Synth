Schema = {
"$schema": "http://json-schema.org/draft-03/schema#",
	"type" : "object",
	"properties": {
		"title" : { "type" : "string" },
		"seed_url": { "type" : "string" },
		"wait_time_after_step" : { "type" : "number" },
		"epoch": { "type": "number" },
		"steps": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"name": { "type": "string" },
					"operation": {
						"type": [ "click", "input" ]
					},
					"DOM_element": {
						"type": "object",
						"properties": {
							"type": [ "string", "null" ],
							"text": [ "string", "null" ],
							"id": [ "string", "null" ],
							"class": [ "string", "null" ],
							"type": [ "string", "null" ]
						}
					}
				}
			}
		}
	}
}