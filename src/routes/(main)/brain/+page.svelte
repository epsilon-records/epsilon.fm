<script lang="ts">
	import Chat from '$lib/components/Chat.svelte';
	import { nanoid } from '$lib/utils';
	import Viewport from '$lib/components/Viewport.svelte';
	const id = nanoid();
</script>

<Viewport>
	<svelte:fragment slot="content"><Chat {id} /></svelte:fragment>
</Viewport>
