<script lang="ts">
	let chat = '';

	async function sendRequest() {
		const response = await fetch('/api/chat', {
			method: 'POST',
			body: JSON.stringify({ messages: [{ role: 'user', content: 'Hello' }] }),
			headers: {
				'content-type': 'application/json'
			}
		});

		chat = await response.text();
	}
</script>

<div>{chat}</div>
<button on:click={sendRequest}>Request</button>
