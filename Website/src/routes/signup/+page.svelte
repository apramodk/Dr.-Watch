<script>
	import { Card, Button, Checkbox } from 'flowbite-svelte';
	import CenterBox from '$lib/CenterBox.svelte';
	import InputGroup from '$lib/InputGroup.svelte';

	let boolProvider = false;
</script>

<main>
	<CenterBox>
		<Card class="w-96">
			<form class="mb-6 flex flex-col space-y-4 align-center" color="dark">
				<InputGroup inputName="Email" />
				<InputGroup inputName="Confirm Email" />
				<InputGroup inputName="Password" />
				<InputGroup inputName="Confirm Password" />
				{#if !boolProvider}
					<InputGroup inputName="Provider Name" />
				{:else if boolProvider}
					<InputGroup inputName="Company" />
				{/if}

				<Checkbox bind:checked={boolProvider}>Are you a provider?</Checkbox>
				<Button outline type="submit">Signup</Button>
			</form>
		</Card>
	</CenterBox>
</main>
