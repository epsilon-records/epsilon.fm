<script lang="ts">
	import '$src/app.css';
	import { Badge } from '$lib/components/ui/badge';
	import { onMount } from 'svelte';

	let networkStatus = navigator.onLine ? 'Connected' : 'Disconnected';

	function updateOnlineStatus() {
		networkStatus = navigator.onLine ? 'Connected' : 'Disconnected';
	}

	onMount(() => {
		window.addEventListener('online', updateOnlineStatus);
		window.addEventListener('offline', updateOnlineStatus);

		return () => {
			window.removeEventListener('online', updateOnlineStatus);
			window.removeEventListener('offline', updateOnlineStatus);
		};
	});
</script>

<Badge variant={networkStatus === 'Connected' ? 'outline' : 'destructive'}>
	{networkStatus === 'Connected' ? '🛜 ' : ''}{networkStatus}
</Badge>
