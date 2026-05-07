import re
from bs4 import BeautifulSoup

with open('mesdasmaes.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Atualizar Title e Meta
soup.title.string = "Especial Mês das Mães — Dra. Isadora Araujo"
meta_desc = soup.find('meta', {'name': 'description'})
if meta_desc:
    meta_desc['content'] = "Campanha especial de Dia das Mães. Combos exclusivos de harmonização facial, botox e preenchimento com a Dra. Isadora Araujo. Parcele em até 12x."

# 2. Atualizar Urgency Bar
urgency_bar = soup.find('div', class_='urgency-bar')
if urgency_bar:
    urgency_bar.string = "🎁 ESPECIAL MÊS DAS MÃES · Condições válidas apenas até 30 de Maio de 2026"

# 3. Atualizar Hero Section
hero_badge = soup.find('div', class_='hero-badge')
if hero_badge:
    hero_badge.string = "Campanha Exclusiva"

hero_h1 = soup.find('h1')
if hero_h1:
    hero_h1.clear()
    hero_h1.append("Sua melhor")
    hero_h1.append(soup.new_tag('br'))
    hero_h1.append("versão começa")
    hero_h1.append(soup.new_tag('br'))
    em = soup.new_tag('em')
    em.string = "aqui"
    hero_h1.append(em)

hero_sub = soup.find('p', class_='hero-sub')
if hero_sub:
    hero_sub.clear()
    hero_sub.append("Neste Dia das Mães, o presente não precisa ser para os outros... ")
    strong = soup.new_tag('strong')
    strong.string = "pode ser pra você."
    hero_sub.append(strong)
    hero_sub.append(" Desenvolvemos protocolos exclusivos para realçar sua beleza natural, elevar sua autoestima e proporcionar resultados elegantes e harmoniosos.")

# Atualizar tags do hero
tags = soup.find_all('span', class_='atag')
if len(tags) >= 3:
    tags[0].string = "Válido até 30/05"
    tags[1].string = "Vagas Limitadas"
    tags[2].string = "Dra. Isadora Araujo"

# Atualizar CTA do hero
hero_cta = soup.find('a', class_='cta-primary')
if hero_cta:
    hero_cta.string = "▶ VER COMBOS ESPECIAIS"
    hero_cta['href'] = "#combos"

# 4. Remover seções não necessárias e adicionar a nova seção de combos
# Vamos manter o Hero, Authority (Tu Instructora), e Footer.
# Vamos substituir o resto pela seção de combos.

# Encontrar o main container ou body
body = soup.body

# Criar nova seção de combos
combos_html = """
<section id="combos" class="pricing-section section" style="background: var(--black); padding-top: 80px;">
  <div class="container">
    <span class="label" style="color: var(--gold); font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-size: 12px;">Especial Dia das Mães</span>
    <h2 class="title" style="font-family: 'Oswald', sans-serif; font-size: 48px; color: var(--white); margin-bottom: 20px; text-transform: uppercase;">Conheça os <em style="color: var(--gold); font-style: normal;">Combos do Mês</em></h2>
    <p class="subtitle" style="color: var(--gray); max-width: 600px; margin: 0 auto 60px; font-size: 18px;">Desenvolvemos protocolos pensados para realçar a beleza natural, elevar a autoestima e proporcionar resultados elegantes e harmoniosos.</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; max-width: 1100px; margin: 0 auto;">
      
      <!-- Combo 1 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Essência de Mãe ✨</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Botox terço médio + preenchimento labial 1ml</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">Um combo de tratamentos estéticos pensados para iluminar a beleza radiante das mães.</p>
        
        <div style="background: rgba(201,168,76,0.1); padding: 10px 15px; border-radius: 4px; margin-bottom: 25px; border-left: 3px solid var(--gold);">
          <span style="color: var(--gold); font-size: 13px; font-weight: 600;">🎁 Ganhe de brinde um peeling de retinóico</span>
        </div>
        
        <div style="margin-bottom: 25px;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 159,00</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 1.299 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Essência de Mãe
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Essência de Mãe." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px; margin-top: auto;">▶ QUERO ESTE COMBO</a>
      </div>

      <!-- Combo 2 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Perfect Lips ✨</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Preenchimento labial (apenas 1ml)</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">Neste Dia das Mães, o presente não precisa ser para os outros... pode ser pra você.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 79,00</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 650,00 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Perfect Lips
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Perfect Lips." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO LÁBIOS PERFEITOS</a>
      </div>

      <!-- Combo 3 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Smooth Skin →</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Somente botox - Terço médio</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">Testa, braço e pés de galinha. 60 unidades distribuídas, toxina melhor do mercado: Letybo.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 88,00</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 799,99 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Smooth Skin
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Smooth Skin." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO PELE LISA</a>
      </div>

      <!-- Combo 4 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo Individual</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Somente 1 ml de ácido hialurônico</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">O Elleva é um bioestimulador de colágeno à base de ácido poli-L-lático (PLLA), que estimula o próprio corpo a produzir colágeno novo.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 89,90</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 850,00 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Individual
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Individual." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO ESTE TRATAMENTO</a>
      </div>

      <!-- Combo 5 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Pele De Boneca</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">3 sessões com intervalo de 21 dias cada</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">O protocolo Pele de Boneca é um tratamento que melhora a textura da pele, reduz manchas, poros e marcas, deixando a pele mais lisa e iluminada.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 47,50</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 350,00 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Pele de Boneca
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Pele de Boneca." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO PELE DE BONECA</a>
      </div>

      <!-- Combo 6 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: 3 mls ✨</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">3 mls de ácido hialurônico</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">Na região indicada ou da sua escolha. Neste Dia das Mães, o presente não precisa ser para os outros... pode ser pra você.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 259,00</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 2.250,00 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo 3 mls
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo 3 mls." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO HARMONIZAR</a>
      </div>

      <!-- Combo 7 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Perfect Plus</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Harmonização full face com 6 mls ou mais...</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">Harmonização Facial full face personalizada para você. A transformação completa que você merece.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">12x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 380,52</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">ou R$ 3.999 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Perfect Plus
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Perfect Plus." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO TRANSFORMAÇÃO COMPLETA</a>
      </div>

      <!-- Combo 8 -->
      <div class="price-box" style="margin: 0; text-align: left; padding: 40px 30px; display: flex; flex-direction: column; height: 100%;">
        <h3 style="color: var(--gold); font-family: 'Oswald', sans-serif; font-size: 24px; margin-bottom: 15px;">Combo: Pele De Boneca + ELLEVA</h3>
        <p style="color: var(--white); font-size: 18px; font-weight: 600; margin-bottom: 10px; line-height: 1.4;">Pele De boneca - Bioestimulador ELLEVA</p>
        <p style="color: var(--gray); font-size: 14px; margin-bottom: 20px; flex-grow: 1;">O Elleva é um bioestimulador de colágeno à base de ácido poli-L-lático (PLLA), que estimula o próprio corpo a produzir colágeno novo.</p>
        
        <div style="margin-bottom: 25px; margin-top: auto;">
          <div style="font-size: 16px; color: var(--gray); margin-bottom: 5px;">10x de</div>
          <div style="font-family: 'Oswald', sans-serif; font-size: 42px; color: var(--white); font-weight: 700; line-height: 1;">R$ 170,00</div>
          <div style="font-size: 14px; color: var(--gold); margin-top: 8px; font-weight: 500;">de <span style="text-decoration: line-through; color: var(--gray);">R$ 1.800</span> por R$ 1.499 à vista</div>
        </div>
        
        <div style="width: 100%; height: 200px; background: #222; border: 1px dashed #444; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; color: #666; font-size: 12px; text-align: center; padding: 20px;">
          [Espaço reservado para foto Antes/Depois]<br>Combo Pele de Boneca + ELLEVA
        </div>
        
        <a href="https://wa.me/5500000000000?text=Olá! Gostaria de agendar o Combo Pele de Boneca + ELLEVA." class="cta-primary" style="width: 100%; font-size: 16px; padding: 15px;">▶ QUERO RENOVAÇÃO PROFUNDA</a>
      </div>

    </div>
  </div>
</section>

<section class="guarantee-section section" style="background: var(--dark); padding: 80px 20px;">
  <div class="container">
    <div class="guarantee-box" style="background: var(--black); border: 2px solid var(--gold); padding: 50px 40px; max-width: 800px; margin: 0 auto; text-align: center;">
      <div style="font-size: 48px; margin-bottom: 20px;">🔒</div>
      <h2 style="font-family: 'Oswald', sans-serif; font-size: 32px; color: var(--white); margin-bottom: 20px; text-transform: uppercase;">Por que escolher a Dra. Isadora?</h2>
      
      <div style="text-align: left; margin-top: 30px;">
        <div style="display: flex; align-items: flex-start; gap: 15px; margin-bottom: 20px;">
          <div style="color: var(--gold); font-size: 24px; line-height: 1;">✓</div>
          <div>
            <h4 style="color: var(--white); font-size: 18px; margin-bottom: 5px;">Resultados Naturais</h4>
            <p style="color: var(--gray); font-size: 15px;">Nossa prioridade é realçar sua beleza, nunca transformá-la em outra pessoa.</p>
          </div>
        </div>
        
        <div style="display: flex; align-items: flex-start; gap: 15px; margin-bottom: 20px;">
          <div style="color: var(--gold); font-size: 24px; line-height: 1;">✓</div>
          <div>
            <h4 style="color: var(--white); font-size: 18px; margin-bottom: 5px;">Produtos Premium</h4>
            <p style="color: var(--gray); font-size: 15px;">Utilizamos apenas as melhores marcas do mercado mundial (como Letybo e Elleva).</p>
          </div>
        </div>
        
        <div style="display: flex; align-items: flex-start; gap: 15px; margin-bottom: 20px;">
          <div style="color: var(--gold); font-size: 24px; line-height: 1;">✓</div>
          <div>
            <h4 style="color: var(--white); font-size: 18px; margin-bottom: 5px;">Segurança em 1º Lugar</h4>
            <p style="color: var(--gray); font-size: 15px;">Procedimentos realizados em ambiente clínico com todos os protocolos de segurança.</p>
          </div>
        </div>
      </div>
      
      <div style="margin-top: 40px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: var(--white); font-size: 16px; margin-bottom: 15px; font-weight: 600;">Formas de Pagamento Seguras</p>
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; font-size: 24px;">
          <span style="background: #fff; color: #1434CB; padding: 5px 10px; border-radius: 4px; font-weight: bold; font-size: 14px;">VISA</span>
          <span style="background: #fff; color: #EB001B; padding: 5px 10px; border-radius: 4px; font-weight: bold; font-size: 14px;">mastercard</span>
          <span style="background: #fff; color: #00A4E0; padding: 5px 10px; border-radius: 4px; font-weight: bold; font-size: 14px;">elo</span>
          <span style="background: #fff; color: #32BCAD; padding: 5px 10px; border-radius: 4px; font-weight: bold; font-size: 14px;">PIX</span>
        </div>
        <p style="color: var(--gray); font-size: 13px; margin-top: 15px;">Parcelamento em até 12x no cartão de crédito. Ambiente 100% seguro.</p>
      </div>
    </div>
  </div>
</section>
"""

# Substituir o conteúdo entre Authority e Footer
# Vamos encontrar a seção Authority
authority_section = soup.find('section', class_='authority-section')

# Vamos encontrar o Footer (final-cta)
final_cta = soup.find('section', class_='final-cta')

if authority_section and final_cta:
    # Remover tudo entre authority e final_cta
    current = authority_section.find_next_sibling()
    while current and current != final_cta:
        next_node = current.find_next_sibling()
        current.extract()
        current = next_node
    
    # Inserir os combos após authority
    combos_soup = BeautifulSoup(combos_html, 'html.parser')
    authority_section.insert_after(combos_soup)

# Atualizar o Final CTA
if final_cta:
    h2 = final_cta.find('h2')
    if h2:
        h2.string = "O seu momento é agora."
    
    p = final_cta.find('p')
    if p:
        p.string = "As condições especiais do Mês das Mães são válidas apenas até o dia 30 de Maio de 2026. Não deixe para depois o cuidado que você merece hoje."
    
    a = final_cta.find('a')
    if a:
        a.string = "▶ AGENDAR MINHA AVALIAÇÃO"
        a['href'] = "https://wa.me/5500000000000?text=Olá! Gostaria de agendar uma avaliação para a campanha de Dia das Mães."

# Salvar o novo HTML
with open('mesdasmaes.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Página mesdasmaes.html gerada com sucesso!")
