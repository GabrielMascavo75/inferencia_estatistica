### Análise: Impacto dos Falsos Negativos em Ambiente Corporativo de TI

Em ambientes conhecidos como SRE (Site Reliability Engineering), os **falsos negativos** representam o erro mais crítico de um modelo preditivo. Um falso negativo ocorre quando o modelo
classifica um servidor com falha iminente como saudável, deixando de emitir o alerta
necessário para ação preventiva.

**Impactos operacionais dos falsos negativos:**

1. **Interrupção não planejada de serviços:** A falha ocorre sem aviso prévio,
   afetando diretamente os usuários e podendo derrubar sistemas críticos.

2. **Perda financeira significativa:** Cada minuto de indisponibilidade pode custar
   milhares de reais, especialmente em setores como e-commerce, finanças e saúde.

3. **Danos à reputação:** Clientes insatisfeitos migram para concorrentes, e
   reconstruir a confiança leva meses ou anos.

4. **Custos de recuperação emergencial:** Manutenção corretiva é significativamente
   mais cara que manutenção preventiva, envolvendo horas extras, plantões e
   possível substituição de hardware.

5. **Efeito cascata:** Um servidor que falha pode sobrecarregar os demais,
   desencadeando falhas em todo o cluster.

6. **Violação de SLA:** Contratos com clientes corporativos estabelecem níveis
   mínimos de disponibilidade, e violá-los pode gerar multas e perda de contratos.

**Trade-off Precisão vs Recall:**

Em SRE, geralmente prioriza-se o **recall** da classe "falha iminente" em detrimento
da precisão, aceitando um número maior de falsos positivos (alarmes falsos) para
garantir que poucas falhas passem despercebidas. Alarmes falsos causam desperdício
de tempo, mas são infinitamente menos custosos que uma interrupção de serviço.

**Aplicação ao nosso modelo:**

Com Recall = 0.84 (exemplo), o modelo deixa passar aproximadamente 16% das falhas
reais. Em um ambiente com 1000 servidores e 10% em risco (100 servidores), isso
significaria ~16 falhas não detectadas — cenário inaceitável para serviços críticos.
Melhorias sugeridas incluem: reduzir K para 3, testar pesos por distância, ou
combinar o modelo com regras heurísticas de monitoramento.

**Conclusão:**

Em produção, um modelo como este deve ser usado como **ferramenta auxiliar**
para a equipe de SRE, nunca como única fonte de decisão. A combinação de
métricas estatísticas, ML e experiência humana é o que garante a confiabilidade
de sistemas críticos.
