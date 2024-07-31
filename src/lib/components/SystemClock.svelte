<script lang="ts">
	import '$src/app.css';
	import { onMount } from 'svelte';
	import { Badge } from '$lib/components/ui/badge';
	import { militaryTimeEnabled } from '$lib/stores/ui';

	let currentTime: string;
	let timezone: string;

	function updateTime() {
		const now = new Date();
		currentTime = now.toLocaleTimeString([], {
			hour: '2-digit',
			minute: '2-digit',
			second: '2-digit',
			hour12: !$militaryTimeEnabled
		});
		timezone =
			new Intl.DateTimeFormat(undefined, { timeZoneName: 'short' })
				.formatToParts(now)
				.find((part) => part.type === 'timeZoneName')?.value || '';
	}

	$: {
		$militaryTimeEnabled;
		updateTime();
	}

	onMount(() => {
		const timer = setInterval(updateTime, 1000);

		return () => {
			clearInterval(timer);
		};
	});
</script>

<Badge variant="outline">🕒 {currentTime} {timezone}</Badge>
