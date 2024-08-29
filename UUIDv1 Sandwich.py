# -*- coding: utf-8 -*-

from burp import IBurpExtender, ITab
from java.awt import Dimension,Toolkit,FlowLayout
from javax.swing import JButton, JFrame,JPanel,BoxLayout,Box,JComboBox,JTextArea,JScrollPane,JSeparator,JLabel,JTextField,JCheckBox
from datetime import datetime, timedelta
import re

class BurpExtender(IBurpExtender, ITab):
    def getTabCaption(self):
        return "UUIDv1 Sandwich"

    def getUiComponent(self):
        # General Panel
        panel = JPanel()
        panel.setLayout(BoxLayout(panel, BoxLayout.Y_AXIS))
        # Box Detect UUIDv1
        box_dt = Box.createHorizontalBox()
        box_dt.setMinimumSize(Dimension(200, 100))
        box_dt.setMaximumSize(Dimension(1000,200))
        panel_detect = JPanel(FlowLayout())
        self.comboBox = JComboBox(['                     DETECTED UUIDv1          '])
        self.comboBox.setEditable(True)
        addbutton = JButton("Add")
        addbutton.setMinimumSize(Dimension(100, 30))
        addbutton.setMaximumSize(Dimension(100, 30))
        addbutton.addActionListener(self.adduuid)
        self.comboBox.addActionListener(self.updateTextField)
        panel_detect.add(addbutton)
        panel_detect.add(self.comboBox)
        self.textArea = JTextArea(7, 30)
        self.textArea.setEditable(False)
        scrollPane = JScrollPane(self.textArea)
        panel_detect.add(scrollPane)
        box_dt.add(panel_detect)
        # Separator
        box_se = Box.createHorizontalBox()
        box_se.setMinimumSize(Dimension(200, 5))
        box_se.setMaximumSize(Dimension(1000,5))
        box_se.add(JSeparator())
        # Box Sandwich Attack
        box_sw = Box.createHorizontalBox()
        box_sw.setMinimumSize(Dimension(250,30))
        box_sw.setMaximumSize(Dimension(250,50))
        panel_sw = JPanel(FlowLayout())
        text = JLabel("SANDWICH ATTACK")
        
        panel_sw.add(text)
        box_sw.add(panel_sw)
        # Box Sandwich function
        box_sw_func = Box.createHorizontalBox()
        box_sw_func.setMinimumSize(Dimension(260, 170))
        box_sw_func.setMaximumSize(Dimension(1000, 200))
        # Vertical1 box
        box_vert1 = Box.createVerticalBox()
        box_vert1.setMinimumSize(Dimension(260, 170))
        box_vert1.setMaximumSize(Dimension(1000, 200))
        vert1_box = JPanel()
        vert1_box.setLayout(BoxLayout(vert1_box, BoxLayout.Y_AXIS))

        # Panel 1
        panel1 = JPanel()
        panel1.setLayout(BoxLayout(panel1, BoxLayout.X_AXIS))
        mac_label = JLabel("Mac Address")
        mac_label.setMaximumSize(Dimension(150, 35))
        self.mac_input = JTextField(10)
        self.mac_input.setText("BA:D0:C0:FF:EE:00")
        self.mac_input.setMinimumSize(Dimension(270, 30))
        self.mac_input.setMaximumSize(Dimension(270, 30))
        panel1.add(mac_label)
        panel1.add(self.mac_input)
        vert1_box.add(panel1)
        # Panel 2
        panel2 = JPanel()
        panel2.setLayout(BoxLayout(panel2, BoxLayout.X_AXIS))
        mac_label = JLabel("Clock Sequence")
        mac_label.setMaximumSize(Dimension(150, 35))
        self.sequence = JTextField(10)
        self.sequence.setText("1111")
        self.sequence.setMinimumSize(Dimension(270, 30))
        self.sequence.setMaximumSize(Dimension(270, 30))
        panel2.add(mac_label)
        panel2.add(self.sequence)
        vert1_box.add(panel2)
        # Panel 3
        panel3 = JPanel()
        panel3.setLayout(BoxLayout(panel3, BoxLayout.X_AXIS))
        time_label = JLabel("Start Time (GMT+0)")
        time_label.setMaximumSize(Dimension(150, 35))
        self.time_input = JTextField(10)
        self.time_input.setText("YYYY-MM-DD HH:mm:SS.sssssss")
        self.time_input.setMinimumSize(Dimension(270, 30))
        self.time_input.setMaximumSize(Dimension(270, 30))
        panel3.add(time_label)
        panel3.add(self.time_input)
        vert1_box.add(panel3)
 
        # Panel 4
        panel4 = JPanel()
        panel4.setLayout(BoxLayout(panel4, BoxLayout.X_AXIS))
        self.tickbox = JCheckBox()
        panel4.add(self.tickbox)
        time_label = JLabel("End Time")
        time_label.setMaximumSize(Dimension(130, 35))
        self.endtime_input = JTextField(10)
        self.endtime_input.setText("YYYY-MM-DD HH:mm:SS.sssssss")
        self.endtime_input.setMinimumSize(Dimension(270, 30))
        self.endtime_input.setMaximumSize(Dimension(270, 30))
        self.endtime_input.setEnabled(False)
        panel4.add(time_label)
        panel4.add(self.endtime_input)
        vert1_box.add(panel4)
        self.tickbox.addActionListener(self.on_tickbox_action)

        # Panel 5 Create
        panel5 = JPanel()
        panel5.setLayout(BoxLayout(panel5, BoxLayout.X_AXIS))
        nothing = JLabel("")
        nothing.setMinimumSize(Dimension(100, 100))
        nothing.setMaximumSize(Dimension(100, 100))
        panel5.add(nothing)
        create = JButton("Create")
        create.setMinimumSize(Dimension(100, 30))
        create.setMaximumSize(Dimension(100, 30))
        create.addActionListener(self.create_wordlist)
        panel5.add(create)
        vert1_box.add(panel5)
    
        box_vert1.add(vert1_box)
        # Vertical2 box
        box_vert2 = Box.createVerticalBox()
        box_vert2.setMinimumSize(Dimension(260, 170))
        box_vert2.setMaximumSize(Dimension(1000, 200))
        # Panel info
        panel_info = JPanel()
        self.info = JTextArea(6,30)
        self.info.setEditable(False)
        scrollinfo = JScrollPane(self.info)
        panel_info.add(scrollinfo)
        copy = JButton("Copy")
        copy.setMinimumSize(Dimension(50, 30))
        copy.setMaximumSize(Dimension(100, 30))
        copy.addActionListener(self.copy_to_clipboard)
        box_vert2.add(panel_info)
        box_vert2.add(copy)
        # Add box_sw_func
        box_sw_func.add(box_vert1)
        box_sw_func.add(box_vert2)
        # Add everything to main panel
        panel.add(box_dt)
        panel.add(box_se)
        panel.add(box_sw)
        panel.add(box_sw_func)

        return panel
    def adduuid(self,event):
        item = self.comboBox.getSelectedItem().strip()
        self.alluuid = [self.comboBox.getItemAt(i) for i in range(self.comboBox.getItemCount())]
        if item in self.alluuid:
            pass
        else:
            uuid_regex = r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'
            if re.match(uuid_regex, item):
                if item[14] != "1":
                    self.textArea.setText("Version {} isn't supported".format(item[14]))
                else:
                    self.comboBox.addItem(item)
                    self.textArea.setText("Success: {}".format(item))
            else:
                self.textArea.setText("Check format uuid\nExample: 28bfc0ee-6125-11ef-a632-0242ac110019")

    def create_wordlist(self,event):
        tmp = False
        mac = self.mac_input.getText().strip()
        if not re.match(r"^[0-9A-Fa-f:]{17}$", mac):
            self.info.setText("Please check MAC Address format\nExemple: 02:42:AC:11:00:20")
            return
        seq = self.sequence.getText().strip()
        if not re.match(r"^[0-9A-Fa-f]{4}$",seq):
            self.info.setText("Please check Clock Sequence format\nExample: a632")
            return
        s_time = self.time_input.getText().strip()
        if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+$", s_time):
            self.info.setText("Please check Start Time format\nExample: 2024-08-23 07:56:09.7114350")
            return
        
        e_time = self.endtime_input.getText().strip()

        if self.tickbox.isSelected():
            if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+$", e_time):
                self.info.setText("Please check End Time format\nExample: 2024-08-23 07:56:09.7114355")
                return
            e_time_p = self.eporch_time(e_time)
            s_time_p = self.eporch_time(s_time)
            if s_time_p < e_time_p:
                data = [self.uuid1(mac, seq, i) for i in range(s_time_p,e_time_p + 1)]
                self.info.setText("\n".join(data))
            else:
                self.info.setText("End Time > Start Time")
        else:
            data = self.uuid1(mac,seq,self.eporch_time(s_time))
            self.info.setText(data)


    def uuid1(self,node,clock_seq,timestamp):
        node = int(node.replace(":",""),16)
        clock_seq = int(clock_seq,16)
        time_low = timestamp & 0xffffffff
        time_mid = (timestamp >> 32) & 0xffff
        time_hi_version = (timestamp >> 48) & 0x0fff
        clock_seq_low = clock_seq & 0xff
        clock_seq_hi_variant = (clock_seq >> 8) & 0x3f
        return self.fields_to_uuid(time_low, time_mid, time_hi_version,clock_seq_hi_variant, clock_seq_low, node)

    def eporch_time(self,submit, GMT=0):
        if '.' in submit:
            submit, nano = submit.split(".")
        else:
            submit, nano = submit, "0000000"
        seconds_since_1582 = int((datetime.strptime(submit, "%Y-%m-%d %H:%M:%S") - datetime(1582, 10, 15)).total_seconds())
        formatted_time = "{}{}".format(seconds_since_1582, nano)
        if len(formatted_time) < len("139436925697100000"):
            formatted_time = formatted_time.ljust(len("139436925697114350"), '0')
        return int(formatted_time) + (GMT * 60 * 60 * 10000000 if GMT <= 14 and GMT >= -12 else 0)
    def fields_to_uuid(self,time_low, time_mid, time_high, clock_seq_high, clock_seq_low, node):
        time_low_hex = '{:08x}'.format(time_low)
        time_mid_hex = '{:04x}'.format(time_mid)
        time_high_and_version_hex = '{:04x}'.format(time_high | 0x1000)
        clock_seq_high_and_reserved_hex = '{:02x}'.format(clock_seq_high | 0x80)
        clock_seq_low_hex = '{:02x}'.format(clock_seq_low)
        node_hex = '{:012x}'.format(node)
        uuid = '{}-{}-{}-{}{}-{}'.format(
            time_low_hex,
            time_mid_hex,
            time_high_and_version_hex,
            clock_seq_high_and_reserved_hex,
            clock_seq_low_hex,
            node_hex
        )
        return uuid
    def copy_to_clipboard(self,event):
        text = self.info.getText()
        string_selection = StringSelection(text)
        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(string_selection, None)


    def on_tickbox_action(self, event):
        self.endtime_input.setEnabled(self.tickbox.isSelected())
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("UUIDv1 Sandwich")
        callbacks.printOutput("UUIDv1 Sandwich")
        callbacks.addSuiteTab(self)
    def stat(self,info):
        dict = {}
        l = info.split("-")
        # Check version
        if l[2][0] == "1":
            dict[info] = [int("".join(l[2][1:]+l[1]+l[0]),16), int(l[3],16), ':'.join(l[4][i:i+2] for i in range(0, 12, 2)).upper(),  int(l[2][0])]
        return dict

    def updateTextField(self, event):
        selected_uuid = self.comboBox.getSelectedItem()
        uuid_regex = r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'
        if re.match(uuid_regex, selected_uuid):
            info_list = self.stat(selected_uuid)
            info = info_list[selected_uuid]
            info_text = (
                "Version: {}\n".format(info[3]) +
                "UUID: {}\n".format(selected_uuid) +
                "Time (GMT +0): {}\n".format(today(info[0])) +
                "Timestamp: {}\n".format(info[0]) +
                "Clock Sequence: {:x}\n".format(info[1]) +
                "MAC Address: {}\n".format(info[2])
            )
            self.textArea.setText(info_text)
    

def today(s, GMT=0):
    s = s + (GMT * 60 * 60 * 10000000 if GMT <= 14 and GMT >= -12 else 0)
    date_part = datetime(1582, 10, 15) + timedelta(seconds=int(str(s)[:-7] + "0" * 7) / 10**7)
    microseconds_part = str(s)[-7:]
    result = "{}.{}".format(date_part.strftime("%Y-%m-%d %H:%M:%S"), microseconds_part)
    return result

