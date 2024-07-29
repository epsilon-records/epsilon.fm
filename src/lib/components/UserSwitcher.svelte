<script lang="ts">
	import UserButton from 'clerk-sveltekit/client/UserButton.svelte';
	import { mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
</script>

{#key $mode}
	<UserButton appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }} />
{/key}
