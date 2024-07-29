<script lang="ts">
	import SignIn from 'clerk-sveltekit/client/SignIn.svelte';
	import { mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
</script>

<div class="m-4 self-center">
	<SignIn
		appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }}
		redirectUrl="/dashboard"
	/>
</div>
