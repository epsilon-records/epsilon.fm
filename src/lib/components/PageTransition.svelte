<script lang="ts">
	import { fade } from 'svelte/transition';

	export let key: string;
	export let duration: number = 100;
</script>

{#key key}
	<div in:fade={{ duration, delay: duration }} out:fade={{ duration }}>
		<slot />
	</div>
{/key}
