<script lang="ts">
	import ClerkLoaded from 'clerk-sveltekit/client/ClerkLoaded.svelte';
	import ClerkLoading from 'clerk-sveltekit/client/ClerkLoading.svelte';
</script>

<ClerkLoading>
	<div class="m-4">Loading...</div>
</ClerkLoading>
<ClerkLoaded let:clerk>
	loaded: {clerk}
	<slot {clerk} />
</ClerkLoaded>
