<script lang="ts">
	import '$src/app.css';
	import { onMount } from 'svelte';
	import { Badge } from '$lib/components/ui/badge';

	let currentTime = new Date().toLocaleTimeString([], {
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
		hour12: true
	});

	onMount(() => {
		const timer = setInterval(() => {
			currentTime = new Date().toLocaleTimeString([], {
				hour: '2-digit',
				minute: '2-digit',
				second: '2-digit',
				hour12: true
			});
		}, 1000);

		return () => {
			clearInterval(timer);
		};
	});
</script>

<Badge variant="outline">🕒 {currentTime}</Badge>
