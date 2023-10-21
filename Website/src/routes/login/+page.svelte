<script>
	import { Card, Button, Checkbox } from 'flowbite-svelte';
	import CenterBox from '$lib/CenterBox.svelte';
	import InputGroup from '$lib/InputGroup.svelte';

	let boolProvider = false;
</script>

<main>
	<CenterBox>
		<Card>
			<form class="mb-6 flex flex-col space-y-4" color="dark">
				<InputGroup inputName="Email" />
				<InputGroup inputName="Password" />

				{#if boolProvider}
					<InputGroup inputName="Provider Name" />
				{:else if boolProvider}
					<InputGroup inputName="Company" />
				{/if}
				<Checkbox bind:checked={boolProvider}>Are you a provider?</Checkbox>
				<Button outline type="submit">Login</Button>
			</form>
		</Card>
	</CenterBox>
</main>
